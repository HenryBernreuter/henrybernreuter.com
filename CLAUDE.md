# henrybernreuter.com — Claude Instructions

Jekyll blog hosted on GitHub Pages. Push to `main` to deploy.

## Adding a New Post

1. Create a file in `_posts/` named `YYYY-MM-DD-title-slug.md`
2. Copy the frontmatter block below and fill in the fields
3. Write the post body in Markdown below the frontmatter
4. Add the Buy Me a Coffee button HTML at the top and bottom of the body (copy from `_drafts/test.md`)
5. **Generate a hero image** — see the Hero Image section below
6. Commit and push to `main` — GitHub Pages rebuilds automatically

### Frontmatter Template

```yaml
---
date: YYYY-MM-DD
layout: post
title: "Post Title Here"
subtitle: "Subtitle here"
description: SEO meta description — one or two sentences, no quotes needed
image: /assets/img/Image_Template_760X399.png
optimized_image: /assets/img/optimized_template_380X200.png
category: tutorial
tags:
  - tag1
  - tag2
toc: true
author: henry
---
```

### Hero Image

Every post needs a 760x399 hero image saved to `assets/img/` named after the post slug (e.g. `when-to-build-an-agent.png`). Update both `image:` and `optimized_image:` in the frontmatter to point to it.

**Option A — Python/PIL (diagrammatic / dark-theme graphics):**
Write a Pillow script (like the one used for the first AI Tooling post) that produces a 760x399 PNG with a dark `#0d1117` background, grid, and a diagram relevant to the post. Run it with `python gen_hero.py`. PIL can be installed with `pip install pillow`.

Example skeleton:
```python
from PIL import Image, ImageDraw, ImageFont
W, H = 760, 399
img = Image.new("RGB", (W, H), "#0d1117")
draw = ImageDraw.Draw(img)
# ... draw your diagram ...
img.save(r"assets\img\your-post-slug.png", "PNG")
```

**Option B — ComfyUI on EC2 (photorealistic / illustrated):**
Submit a job to the ComfyUI pipeline at `http://100.51.156.222:8188` using the Qwen Image Edit model. Resize/crop output to 760x399 before saving to `assets/img/`.

**Note:** The `optimized_image` field is supposed to be 380x200, but using the same 760x399 image for both fields works fine in practice.

### Categories in use
- `tutorial` — how-to posts
- `ai-engineering` — agents, LLMs, tooling
- `data` — data science, pandas, visualization

### Images
- Drop images in `assets/img/`
- Reference as `/assets/img/filename.png`
- The `image` field is the card thumbnail (760x399); `optimized_image` is the smaller version (380x200)
- Until real images are added, use the template placeholders in the frontmatter above

## Series: AI Tooling Decision Framework

Posts in order — each builds on the last:

| # | Title | File | Status |
|---|-------|------|--------|
| 1 | When to Build an Agent (And When You're Overcomplicating It) | `2026-07-06-when-to-build-an-agent.md` | Published |
| 2 | LangChain vs. Raw API vs. Writing It Yourself | TBD | Planned |
| 3 | Evaluating Agents in Production | TBD | Planned |

## Deployment

```bash
git add _posts/YYYY-MM-DD-your-post.md
git commit -m "Add post: Your Post Title"
git push origin main
```

GitHub Pages typically rebuilds within 1–2 minutes. Check `https://www.henrybernreuter.com` to confirm the post appears.