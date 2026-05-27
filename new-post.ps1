#Requires -Version 5.1
<#
.SYNOPSIS
    Drafts a new Jekyll blog post using the Claude API.
.PARAMETER Topic
    The topic or title idea for the post (required).
.PARAMETER Outline
    Optional bullet points or outline to guide the content.
.PARAMETER Category
    Post category: tutorial, blog, or portfolio. Defaults to 'tutorial'.
.PARAMETER Tags
    Space-separated tags. If omitted, Claude will suggest some.
.EXAMPLE
    .\new-post.ps1 -Topic "Pandas merge vs join explained"
    .\new-post.ps1 -Topic "Visualizing Time Series" -Outline "- use matplotlib\n- seasonal decomposition\n- anomaly highlighting" -Category blog
#>
param(
    [Parameter(Mandatory)]
    [string]$Topic,

    [string]$Outline = "",

    [ValidateSet("tutorial", "blog", "portfolio")]
    [string]$Category = "tutorial",

    [string]$Tags = ""
)

# ── API key ──────────────────────────────────────────────────────────────────
$apiKey = $env:ANTHROPIC_API_KEY
if (-not $apiKey) {
    Write-Error "ANTHROPIC_API_KEY environment variable is not set. Set it with: `$env:ANTHROPIC_API_KEY = 'sk-ant-...'"
    exit 1
}

# ── Prompt ───────────────────────────────────────────────────────────────────
$systemPrompt = @"
You are a writing assistant for HenryBernreuter.com, a data science and data engineering blog.
Henry is a data engineer and data scientist. Posts are practical, code-forward, and friendly in tone.

Given a topic, return a JSON object (no markdown fences, raw JSON only) with these fields:
{
  "title": "The post title",
  "subtitle": "One-sentence hook, under 80 characters",
  "description": "SEO-friendly description, under 120 characters",
  "suggested_tags": "space-separated lowercase tags relevant to the post",
  "body": "Full post body in Markdown. Use ## and ### for headers. Include Python/R code examples in fenced code blocks where relevant. 700-1000 words. First person occasionally. No YAML front matter."
}

Guidelines for the body:
- Open with a short practical hook (not 'In this post we will...')
- Use real, runnable code examples
- Close with a takeaway or what to try next
- Write for someone who already knows some Python/R but wants a clearer mental model
"@

$userMessage = "Topic: $Topic"
if ($Outline) {
    $userMessage += "`n`nKey points to cover:`n$Outline"
}
if ($Category -eq "portfolio") {
    $userMessage += "`n`nThis is a portfolio/project post, not a tutorial. Describe the project, the problem solved, and the approach."
}

# ── API call ──────────────────────────────────────────────────────────────────
$requestBody = @{
    model      = "claude-sonnet-4-6"
    max_tokens = 3000
    system     = $systemPrompt
    messages   = @(@{ role = "user"; content = $userMessage })
} | ConvertTo-Json -Depth 5

Write-Host "Drafting post about: $Topic" -ForegroundColor Cyan
Write-Host ""

try {
    $response = Invoke-RestMethod `
        -Uri "https://api.anthropic.com/v1/messages" `
        -Method POST `
        -Headers @{
            "x-api-key"         = $apiKey
            "anthropic-version" = "2023-06-01"
            "content-type"      = "application/json"
        } `
        -Body $requestBody
} catch {
    Write-Error "API call failed: $($_.Exception.Message)"
    exit 1
}

$rawText = $response.content[0].text

# ── Parse JSON response ───────────────────────────────────────────────────────
try {
    $parsed = $rawText | ConvertFrom-Json
} catch {
    Write-Error "Claude returned unexpected output. Raw response saved to new-post-debug.txt"
    $rawText | Out-File "new-post-debug.txt" -Encoding utf8
    exit 1
}

$title       = $parsed.title
$subtitle    = $parsed.subtitle
$description = $parsed.description
$body        = $parsed.body
$finalTags   = if ($Tags) { $Tags } else { $parsed.suggested_tags }

# ── Build Jekyll file ─────────────────────────────────────────────────────────
$slug = $title.ToLower() `
    -replace "[^a-z0-9\s-]", "" `
    -replace "\s+", "-" `
    -replace "-+", "-"
$slug = $slug.Trim("-")

$date     = Get-Date -Format "yyyy-MM-dd"
$dateTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$filename = "_posts\$date-$slug.md"

$frontMatter = @"
---
date: $dateTime
layout: post
title: $title
subtitle: $subtitle
description: $description
image: /assets/img/Image_Template_760X399.png
optimized_image: /assets/img/optimized_template_380X200.png
category: $Category
tags: $finalTags
toc: true
author: henry
---

"@

Set-Content -Path $filename -Value ($frontMatter + $body) -Encoding utf8

# ── Summary ───────────────────────────────────────────────────────────────────
Write-Host "Done!" -ForegroundColor Green
Write-Host ""
Write-Host "  File:     $filename" -ForegroundColor Yellow
Write-Host "  Title:    $title"    -ForegroundColor Yellow
Write-Host "  Subtitle: $subtitle" -ForegroundColor Yellow
Write-Host "  Tags:     $finalTags" -ForegroundColor Yellow
Write-Host ""
Write-Host "Review and edit the file, then commit to publish." -ForegroundColor Cyan
