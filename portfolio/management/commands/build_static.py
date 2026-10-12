"""
python manage.py build_static [--out dist]

Renders every page to plain HTML so the site can be hosted on GitHub Pages.
"""
import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.test import Client

from portfolio import content


class Command(BaseCommand):
    help = "Render the whole site to static HTML (for GitHub Pages)."

    def add_arguments(self, parser):
        parser.add_argument("--out", default="dist")

    def handle(self, *args, out="dist", **opts):
        settings.DEBUG = False
        out = Path(settings.BASE_DIR) / out
        if out.exists():
            shutil.rmtree(out)
        out.mkdir(parents=True)
        client = Client(HTTP_HOST="localhost")

        paths = ["/", "/blog/", "/about/", "/contact/", "/privacy-policy/", "/terms/", "/disclaimer/",
                 "/search-index.json", "/sitemap.xml", "/feed.xml", "/robots.txt", "/ads.txt", "/404.html"]
        posts = content.all_posts()
        pages = max(1, -(-len(posts) // 9))
        paths += [f"/blog/page/{n}/" for n in range(2, pages + 1)]
        paths += [p.path for p in posts]
        paths += [f"/blog/category/{c['slug']}/" for c in content.categories()]

        for path in paths:
            r = client.get(path)
            if r.status_code != 200:
                self.stderr.write(f"! {path} -> {r.status_code}")
                continue
            target = out / path.lstrip("/")
            if path.endswith("/"):
                target = target / "index.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(r.content)
            self.stdout.write(f"  {path}")

        shutil.copytree(Path(settings.BASE_DIR) / "static", out / "static")
        (out / ".nojekyll").write_text("")          # tell GitHub Pages not to run Jekyll
        domain = settings.SITE["custom_domain"]
        if domain:
            (out / "CNAME").write_text(domain + "\n")
        self.stdout.write(self.style.SUCCESS(f"Built {len(paths)} pages -> {out}"))
