import json
from datetime import datetime, time, timezone

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from . import content, data

PER_PAGE = 9


def _abs(path):
    return settings.SITE["url"] + path


def home(request):
    posts = content.all_posts()
    sections = {
        "projects": data.PROJECTS, "seasons": data.SEASONS, "picks": data.TOP_PICKS,
        "skills": data.SKILL_CATEGORIES, "achievements": data.ACHIEVEMENTS,
    }
    ctx = {
        "is_home": True, "d": data, "latest_posts": posts[:3], "stats": {
            "projects": len(data.PROJECTS),
            "episodes": sum(len(s["episodes"]) for s in data.SEASONS),
            "seasons": len(data.SEASONS),
            "posts": len(posts),
            "certs": len(data.CERTIFICATIONS),
            "achievements": len(data.ACHIEVEMENTS),
        },
        "evidence": data.SKILL_EVIDENCE,
        "intro_slides": data.INTRO_SLIDES,
        "viewer_profiles": data.VIEWER_PROFILES,
        "projects_data": data.PROJECTS,
        "title": f"{data.PROFILE['full_name']} — Full Stack Developer & AI/ML Engineer",
        "description": data.PROFILE["intro"],
        **sections,
    }
    return render(request, "home.html", ctx)


def _paginate(items, page):
    pages = max(1, -(-len(items) // PER_PAGE))
    page = max(1, min(page, pages))
    chunk = items[(page - 1) * PER_PAGE: page * PER_PAGE]
    return chunk, page, pages


def blog_list(request, page=1):
    chunk, page, pages = _paginate(content.all_posts(), page)
    return render(request, "blog/list.html", {
        "posts": chunk, "page": page, "pages": pages, "page_range": range(1, pages + 1),
        "categories": content.categories(),
        "title": "Blog — Programming, Open Source & Cloud Notes",
        "description": "Practical tutorials and notes on Django, Flask, open source and cloud by Aditya Aryan.",
    })


def blog_category(request, slug):
    cats = {c["slug"]: c for c in content.categories()}
    posts = [p for p in content.all_posts() if p.category_slug == slug]
    name = cats[slug]["name"] if slug in cats else slug
    return render(request, "blog/list.html", {
        "posts": posts, "page": 1, "pages": 1, "categories": content.categories(), "active_category": slug,
        "heading": name, "title": f"{name} — Blog", "description": f"Articles in {name} by Aditya Aryan.",
    })


def blog_detail(request, slug):
    post = content.get_post(slug)
    posts = content.all_posts()
    i = posts.index(post)
    related = [p for p in posts if p is not post and (p.category == post.category or set(p.tags) & set(post.tags))][:3]
    url = _abs(post.path)
    ld = {
        "@context": "https://schema.org", "@type": "BlogPosting", "headline": post.title,
        "description": post.description, "datePublished": post.date.isoformat(),
        "dateModified": post.updated.isoformat(), "mainEntityOfPage": url,
        "author": {"@type": "Person", "name": data.PROFILE["full_name"], "url": settings.SITE["url"] + "/about/"},
        "publisher": {"@type": "Person", "name": data.PROFILE["full_name"]},
        "image": _abs("/static/img/og-image.png"), "keywords": ", ".join(post.tags),
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": settings.SITE["url"] + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": _abs("/blog/")},
            {"@type": "ListItem", "position": 3, "name": post.title, "item": url}]}
    return render(request, "blog/detail.html", {
        "post": post, "related": related,
        "newer": posts[i - 1] if i > 0 else None, "older": posts[i + 1] if i + 1 < len(posts) else None,
        "title": post.title, "description": post.description, "og_type": "article",
        "jsonld": json.dumps([ld, crumbs]),
    })


def about(request):
    return render(request, "pages/about.html", {"d": data, "title": "About Aditya Aryan",
                  "description": "About Aditya Aryan: B.Tech AI & ML student, IIT Madras Data Science scholar and full stack developer."})


def contact(request):
    return render(request, "pages/contact.html", {"title": "Contact", "description": "Get in touch with Aditya Aryan."})


def privacy(request):
    return render(request, "pages/privacy.html", {"title": "Privacy Policy", "description": "How this site handles data, cookies and advertising.",
                                                  "updated": datetime.now().strftime("%B %d, %Y")})


def terms(request):
    return render(request, "pages/terms.html", {"title": "Terms of Use", "description": "Terms of use for this website."})


def disclaimer(request):
    return render(request, "pages/disclaimer.html", {"title": "Disclaimer", "description": "Disclaimer for content published on this website."})


def not_found(request):
    return render(request, "404.html", {"title": "Page not found", "noindex": True})


def search_index(request):
    items = [{"t": p.title, "u": settings.SITE["base_path"] + p.path, "d": p.description,
              "c": p.category, "g": p.tags, "date": p.date.isoformat()} for p in content.all_posts()]
    return HttpResponse(json.dumps(items), content_type="application/json")


def robots(request):
    s = settings.SITE
    return HttpResponse(f"User-agent: *\nAllow: /\n\nSitemap: {s['url']}/sitemap.xml\n", content_type="text/plain")


def ads_txt(request):
    client = settings.SITE["adsense_client"].replace("ca-", "")
    body = f"google.com, {client}, DIRECT, f08c47fec0942fa0\n" if client else "# Add ADSENSE_CLIENT to generate this file\n"
    return HttpResponse(body, content_type="text/plain")


def sitemap(request):
    s = settings.SITE["url"]
    urls = [("/", None, "1.0"), ("/blog/", None, "0.9"), ("/about/", None, "0.6"), ("/contact/", None, "0.4"),
            ("/privacy-policy/", None, "0.3"), ("/terms/", None, "0.3"), ("/disclaimer/", None, "0.3")]
    for c in content.categories():
        urls.append((f"/blog/category/{c['slug']}/", None, "0.5"))
    for p in content.all_posts():
        urls.append((p.path, p.updated.isoformat(), "0.8"))
    rows = "".join(f"<url><loc>{s}{u}</loc>{f'<lastmod>{m}</lastmod>' if m else ''}<priority>{pr}</priority></url>" for u, m, pr in urls)
    xml = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{rows}</urlset>'
    return HttpResponse(xml, content_type="application/xml")


def feed(request):
    s = settings.SITE
    items = ""
    for p in content.all_posts()[:20]:
        pub = datetime.combine(p.date, time(), tzinfo=timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
        items += (f"<item><title>{_esc(p.title)}</title><link>{s['url']}{p.path}</link><guid>{s['url']}{p.path}</guid>"
                  f"<pubDate>{pub}</pubDate><description>{_esc(p.description)}</description></item>")
    xml = (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{_esc(s["name"])} — Blog</title>'
           f'<link>{s["url"]}/blog/</link><description>Notes on Django, Flask, open source and cloud.</description>{items}</channel></rss>')
    return HttpResponse(xml, content_type="application/rss+xml")


def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
