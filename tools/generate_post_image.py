"""
generate_post_image.py

Calls the local ComfyUI API to generate hero + thumbnail images for blog posts,
then saves them directly to assets/img/.

Usage:
    python tools/generate_post_image.py --post sklearn
    python tools/generate_post_image.py --post numpy
    python tools/generate_post_image.py --post pandas

Requirements:
    pip install requests
    ComfyUI must be running at http://127.0.0.1:8188
"""

import argparse
import json
import random
import shutil
import time
from pathlib import Path

import requests

# ── Config ────────────────────────────────────────────────────────────────────

COMFY_URL      = "http://127.0.0.1:8000"
COMFY_OUTPUT   = Path(r"C:\Users\bernr\Documents\ComfyUI\output")
WORKFLOW_FILE  = Path(r"C:\Users\bernr\Documents\ComfyUI\user\default\workflows\post_image_workflow.json")
ASSETS_DIR     = Path(__file__).parent.parent / "assets" / "img"
CHECKPOINT     = "sd_xl_base_1.0.safetensors"

NEGATIVE = (
    "text, watermark, logo, signature, username, words, letters, typography, "
    "blurry, low quality, jpeg artifacts, cropped, worst quality, bad anatomy, "
    "cluttered, busy background, photorealistic face, person, human"
)

# ── Post prompts ──────────────────────────────────────────────────────────────
# SD 1.5 style: comma-separated keywords, quality boosters first
# Hero: 768x432 (16:9)  |  Thumb: 512x320 (16:10, close enough for cards)

POSTS = {
    "sklearn": {
        "hero": (
            "masterpiece, best quality, highly detailed, digital concept art, "
            "machine learning decision tree visualization, glowing orange and blue nodes "
            "connected by thin luminous lines, dark navy background, minimalist geometric, "
            "data science abstract art, soft neon glow, clean edges, 8k, sharp"
        ),
        "thumb": (
            "masterpiece, best quality, digital art, close-up glowing orange nodes, "
            "decision tree branches, dark navy background, blue accent light, "
            "minimalist tech illustration, sharp"
        ),
    },
    "numpy": {
        "hero": (
            "masterpiece, best quality, highly detailed, digital concept art, "
            "abstract numerical grid floating in dark space, glowing blue matrix of numbers, "
            "multidimensional array visualization, cyan and white light, dark background, "
            "mathematical beauty, clean geometric, 8k, sharp"
        ),
        "thumb": (
            "masterpiece, best quality, digital art, glowing blue numerical array grid, "
            "dark background, cyan light, abstract math visualization, sharp, clean"
        ),
    },
    "pandas": {
        "hero": (
            "masterpiece, best quality, highly detailed, digital concept art, "
            "abstract data table visualization, glowing rows and columns of structured data, "
            "teal and orange light on dark background, clean spreadsheet aesthetic, "
            "data engineering concept art, 8k, sharp"
        ),
        "thumb": (
            "masterpiece, best quality, digital art, glowing teal data grid, "
            "structured rows and columns, dark background, orange accent, "
            "clean data visualization, sharp"
        ),
    },
    "matplotlib": {
        "hero": (
            "masterpiece, best quality, highly detailed, digital concept art, "
            "beautiful glowing data charts floating in dark space, line charts bar charts scatter plots, "
            "multicolor neon light blue green orange, dark background, "
            "data visualization abstract art, 8k, sharp"
        ),
        "thumb": (
            "masterpiece, best quality, digital art, glowing multicolor line chart, "
            "dark background, neon data visualization, blue orange green light, sharp"
        ),
    },
    "langchain": {
        "hero": (
            "masterpiece, best quality, highly detailed, digital concept art, "
            "glowing chain links connecting AI nodes, LLM pipeline visualization, "
            "purple and gold light, dark background, abstract AI orchestration, "
            "neural network aesthetic, 8k, sharp"
        ),
        "thumb": (
            "masterpiece, best quality, digital art, glowing chain of light connecting nodes, "
            "purple gold, dark background, AI pipeline abstract, sharp"
        ),
    },
    "huggingface": {
        "hero": (
            "masterpiece, best quality, highly detailed, digital concept art, "
            "abstract neural network layers glowing in warm amber and yellow light, "
            "transformer architecture visualization, dark background, flowing data streams, "
            "AI model concept art, 8k, sharp"
        ),
        "thumb": (
            "masterpiece, best quality, digital art, glowing amber neural network, "
            "transformer layers, dark background, warm yellow light, sharp"
        ),
    },
    "fastapi": {
        "hero": (
            "masterpiece, best quality, highly detailed, digital concept art, "
            "glowing API endpoint routes visualization, green neon request arrows, "
            "dark background, REST API abstract art, teal and green light, "
            "server architecture concept, 8k, sharp"
        ),
        "thumb": (
            "masterpiece, best quality, digital art, glowing green API route paths, "
            "dark background, teal neon, server concept art, sharp"
        ),
    },
    "databricks": {
        "hero": (
            "masterpiece, best quality, highly detailed, digital concept art, "
            "massive data lakehouse visualization, glowing delta lake storage layers, "
            "Apache Spark cluster nodes connected by streaming data rivers, "
            "red and orange light on dark background, enterprise data platform, "
            "cloud architecture abstract art, 8k, sharp"
        ),
        "thumb": (
            "masterpiece, best quality, digital art, glowing red orange data streams, "
            "Spark cluster nodes, dark background, data lakehouse abstract, sharp"
        ),
    },
    "tensorflow": {
        "hero": (
            "masterpiece, best quality, highly detailed, digital concept art, "
            "deep neural network visualization, orange flowing data through layered nodes, "
            "dark background, gradient descent abstract, machine learning architecture, "
            "glowing computational graph, 8k, sharp"
        ),
        "thumb": (
            "masterpiece, best quality, digital art, orange glowing neural network layers, "
            "dark background, deep learning abstract, computational graph, sharp"
        ),
    },
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def build_api_prompt(positive: str, negative: str, width: int, height: int, filename_prefix: str) -> dict:
    """Convert workflow to ComfyUI API format with injected values."""
    return {
        "4": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {"ckpt_name": CHECKPOINT}
        },
        "6": {
            "class_type": "CLIPTextEncode",
            "inputs": {"text": positive, "clip": ["4", 1]}
        },
        "7": {
            "class_type": "CLIPTextEncode",
            "inputs": {"text": negative, "clip": ["4", 1]}
        },
        "5": {
            "class_type": "EmptyLatentImage",
            "inputs": {"width": width, "height": height, "batch_size": 1}
        },
        "3": {
            "class_type": "KSampler",
            "inputs": {
                "model": ["4", 0],
                "positive": ["6", 0],
                "negative": ["7", 0],
                "latent_image": ["5", 0],
                "seed": random.randint(0, 2**32),
                "steps": 25,
                "cfg": 7.5,
                "sampler_name": "euler",
                "scheduler": "normal",
                "denoise": 1.0
            }
        },
        "8": {
            "class_type": "VAEDecode",
            "inputs": {"samples": ["3", 0], "vae": ["4", 2]}
        },
        "9": {
            "class_type": "SaveImage",
            "inputs": {"images": ["8", 0], "filename_prefix": filename_prefix}
        }
    }


def queue_prompt(workflow_api: dict) -> str:
    response = requests.post(f"{COMFY_URL}/prompt", json={"prompt": workflow_api}, timeout=30)
    response.raise_for_status()
    return response.json()["prompt_id"]


def wait_for_image(prompt_id: str, timeout: int = 300) -> str:
    print(f"  Waiting for generation (prompt_id: {prompt_id[:8]}...)  ", end="", flush=True)
    start = time.time()
    while time.time() - start < timeout:
        history = requests.get(f"{COMFY_URL}/history/{prompt_id}", timeout=10).json()
        if prompt_id in history:
            outputs = history[prompt_id]["outputs"]
            images = outputs["9"]["images"]
            print("done.")
            return images[0]["filename"]
        print(".", end="", flush=True)
        time.sleep(2)
    raise TimeoutError(f"Generation timed out after {timeout}s")


def copy_to_assets(comfy_filename: str, dest_name: str) -> Path:
    src = COMFY_OUTPUT / comfy_filename
    dest = ASSETS_DIR / dest_name
    shutil.copy2(src, dest)
    print(f"  Saved -> {dest}")
    return dest


def generate(post: str, kind: str):
    prompts = POSTS[post]
    positive = prompts[kind]
    filename_prefix = f"{post}-{kind}"

    if kind == "hero":
        width, height = 1024, 576   # SDXL native 16:9
    else:
        width, height = 768, 448    # SDXL native thumbnail

    print(f"\n[{post}] Generating {kind} ({width}x{height})...")
    workflow_api = build_api_prompt(positive, NEGATIVE, width, height, filename_prefix)
    prompt_id = queue_prompt(workflow_api)
    comfy_filename = wait_for_image(prompt_id)
    copy_to_assets(comfy_filename, f"{filename_prefix}.png")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate blog post images via ComfyUI")
    parser.add_argument("--post", required=True, choices=list(POSTS.keys()),
                        help="Which post to generate images for")
    parser.add_argument("--type", choices=["hero", "thumb", "both"], default="both",
                        help="Which image type to generate (default: both)")
    args = parser.parse_args()

    try:
        requests.get(f"{COMFY_URL}/system_stats", timeout=5)
    except Exception:
        print("ERROR: ComfyUI is not running at http://127.0.0.1:8188")
        print("Start ComfyUI first, then run this script.")
        return

    if args.type in ("hero", "both"):
        generate(args.post, "hero")
    if args.type in ("thumb", "both"):
        generate(args.post, "thumb")

    print(f"\nDone. Images saved to assets/img/")
    print(f"Update the post front matter:")
    print(f"  image: /assets/img/{args.post}-hero.png")
    print(f"  optimized_image: /assets/img/{args.post}-thumb.png")


if __name__ == "__main__":
    main()
