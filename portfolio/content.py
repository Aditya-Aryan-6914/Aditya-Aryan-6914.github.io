"""Loads blog posts from content/posts/*.md (YAML front matter + Markdown body)."""
import datetime as dt
import re
from functools import lru_cache
from pathlib import Path

import markdown
import yaml
from django.conf import settings
from django.utils.text import slugify

POSTS_DIR = Path(settings.BASE_DIR) / "content" / "posts"
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.S)


def _date(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    return dt.date.fromisoformat(str(v))


class Post:
    def __init__(self, path: Path):
        raw = path.read_text(encoding="utf-8")
        m = FM.match(raw)
        if not m:
            raise ValueError(f"{path.name}: missing front matter (--- ... ---)")
        meta, body = yaml.safe_load(m.group(1)) or {}, m.group(2)
        self.title = meta["title"]
        self.slug = meta.get("slug") or slugify(path.stem)
        self.date = _date(meta["date"])
        self.updated = _date(meta.get("updated", meta["date"]))
        self.category = meta.get("category", "General")
        self.category_slug = slugify(self.category)
        self.tags = meta.get("tags", [])
        self.description = meta["description"]
        self.draft = bool(meta.get("draft", False))
        self.cover = meta.get("cover")
        self.body_md = body
        md = markdown.Markdown(extensions=["fenced_code", "tables", "toc", "sane_lists"],
                               extension_configs={"toc": {"toc_depth": "2-3"}})
        self.html = md.convert(body)
        self.toc = md.toc_tokens
        self.words = len(re.findall(r"\w+", body))
        self.reading_minutes = max(1, round(self.words / 220))

    @property
    def path(self):
        return f"/blog/{self.slug}/"


@lru_cache(maxsize=1)
def all_posts():
    posts = [Post(p) for p in sorted(POSTS_DIR.glob("*.md"))]
    posts = [p for p in posts if not p.draft and p.date <= dt.date.today()]
    return sorted(posts, key=lambda p: p.date, reverse=True)


def get_post(slug):
    return next((p for p in all_posts() if p.slug == slug), None)


def categories():
    out = {}
    for p in all_posts():
        c = out.setdefault(p.category_slug, {"name": p.category, "slug": p.category_slug, "count": 0})
        c["count"] += 1
    return sorted(out.values(), key=lambda c: c["name"])
