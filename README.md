# Aditya Aryan — Portfolio + Blog (Django → GitHub Pages)

A cinematic, streaming-style portfolio with a SEO-ready blog. **Django is used as a static site generator**:
`python manage.py build_static` renders every page to plain HTML in `dist/`, and a GitHub Action publishes it to GitHub Pages.
(GitHub Pages cannot run Django itself, so there is no database; blog posts are Markdown files.)

## 1. Run locally
```bash
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver                              # live preview at http://127.0.0.1:8000
python manage.py build_static --out dist                # build the static site
python -m http.server -d dist 8080                      # preview the built output
```

## 2. Put your details in
| What | Where |
| --- | --- |
| Name, bio, links, **email, LinkedIn**, education, projects, skills, journey | `portfolio/data.py` (anything set to `None` is hidden) |
| Photo | save as `static/img/portrait.png` (transparent PNG cut-out looks best) or `.webp/.jpg` |
| Resume PDF | `static/files/Aditya_Aryan_Resume.pdf` (button appears automatically) |
| Site-wide settings | `config/settings.py` → `SITE`, or GitHub repo **Variables** (below) |

## 3. Write blog posts
Add a file to `content/posts/my-post.md`:
```markdown
---
title: "Post title"
date: 2026-10-12            # future dates stay hidden until that day (daily rebuild publishes them)
category: Django
tags: [django, python]
description: "150–160 character summary used for Google results and social cards."
draft: false
---
Your Markdown here. Use ## headings, code fences, tables.
```
Push to `main` and the site rebuilds.

## 4. Deploy on GitHub Pages
1. Create a GitHub repo and push this project to the `main` branch.
2. **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. The workflow in `.github/workflows/deploy.yml` builds and deploys. Your URL will be one of:
   * Repo named `Aditya-Aryan-6914.github.io` → `https://aditya-aryan-6914.github.io/`  *(recommended, no sub-path)*
   * Any other repo name → `https://aditya-aryan-6914.github.io/<repo>/` *(handled automatically via `BASE_PATH`)*
   * Custom domain → add repo variable `CUSTOM_DOMAIN` (e.g. `blog.adityaaryan.me`) and point DNS to GitHub Pages.

### Optional repo variables (Settings → Secrets and variables → Actions → **Variables**)
| Variable | Purpose |
| --- | --- |
| `CUSTOM_DOMAIN` | custom domain (writes `CNAME`, fixes canonical/sitemap URLs) |
| `ADSENSE_CLIENT` | `ca-pub-XXXXXXXXXXXXXXXX` — adds the AdSense script and generates `ads.txt` |
| `ADSENSE_SLOT` | optional ad unit id for in-article ads (Auto ads work without it) |
| `GA_ID` | Google Analytics 4 id (`G-…`), loaded only after cookie consent |
| `GSC_TOKEN` | Google Search Console verification meta value |
| `FORMSPREE_ENDPOINT` | contact form endpoint from formspree.io |

## 5. SEO checklist (already built in)
Canonical URLs · Open Graph/Twitter cards · JSON-LD (Person, WebSite, BlogPosting, Breadcrumbs) · `sitemap.xml` · `robots.txt` · RSS `feed.xml` · semantic HTML, one `h1` per page · fast static pages · mobile-first · 404 page.
After deploying: add the site in **Google Search Console**, submit `/sitemap.xml`, then request indexing for your best posts.

## 6. Getting AdSense-approved (honest checklist)
Approval is decided by Google, so nothing can guarantee it, but these are the usual requirements:
* **Original, useful content**: aim for 15–25 well-written posts (600+ words, written by you) before applying. Three starter posts are included; replace/extend them.
* **Required pages** are included: About, Contact, Privacy Policy, Terms, Disclaimer.
* **Own your domain**: AdSense generally does not approve `*.github.io` subdomains. Buy a domain (e.g. `adityaaryan.me`/`blog.adityaaryan.me`) and set `CUSTOM_DOMAIN`.
* Clear navigation, no broken links, no copied/AI-spun text, no placeholder "lorem ipsum".
* Be 18+, have a real name/address for payments, and apply with the domain verified.
* After approval, set `ADSENSE_CLIENT`; `ads.txt` is generated automatically.
