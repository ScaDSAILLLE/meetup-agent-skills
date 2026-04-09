---
name: wikipedia-browser-surf
description: Open the system default browser and navigate to Wikipedia with optional topic search. Use when users ask to open Wikipedia, browse wikipedia.org, or search a topic on Wikipedia. If no topic is provided, opens the Wikipedia start page; if a topic is provided, opens Wikipedia search results.
---

# Wikipedia Browser Surf

Open the system default browser, go to Wikipedia, and optionally search a topic.

## When to Use This Skill

- User asks to open Wikipedia in a browser.
- User asks to browse Wikipedia manually.
- User asks to search a topic on Wikipedia and keep the browser open.

## Prerequisites

- Python 3.9+

## Step-by-Step Workflow

1. Ask for an optional topic and optional language code.
2. Run the bundled script:
   - No topic: `python scripts/open_wikipedia.py`
   - Topic: `python scripts/open_wikipedia.py --topic "Alan Turing"`
   - German Wikipedia: `python scripts/open_wikipedia.py --topic "Leipzig" --lang de`
3. Confirm URL was opened in the user's default browser.

## Guardrails

- Default language is English (`--lang en`), but any Wikipedia language code can be used.
- Only navigate to Wikipedia domains.
- Keep behavior simple: open homepage or search results page.
- Do not claim extraction/scraping unless explicitly implemented.

## Validation Checklist

- Script opens the system browser successfully.
- No topic opens `https://www.wikipedia.org`.
- With topic opens language-specific Wikipedia search URL with the provided query.

## Troubleshooting

- If browser does not open, verify default browser settings.
- On Linux, ensure `xdg-open` is available.
- In WSL/Windows environments, ensure `cmd.exe` is callable.
