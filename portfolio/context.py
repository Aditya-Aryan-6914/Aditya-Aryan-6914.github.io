import os
from django.conf import settings


def site(request):
    s = settings.SITE
    portrait = None
    for name in ("img/portrait.webp", "img/portrait.png", "img/portrait.jpg", "img/portrait.jpeg"):
        if os.path.exists(os.path.join(settings.BASE_DIR, "static", name)):
            portrait = name
            break
    from . import data
    resume = data.PROFILE["resume_pdf"]
    resume_ok = bool(resume) and os.path.exists(os.path.join(settings.BASE_DIR, "static", resume))
    og = "img/og-image.png"
    return {
        "SITE": s,
        "BASE": s["base_path"],
        "PORTRAIT": portrait,
        "RESUME_URL": resume if resume_ok else None,
        "OG_IMAGE": s["url"] + "/static/" + og,
        "CANONICAL": s["url"] + request.path.replace(s["base_path"], "", 1) if request.path != "/404.html" else "",
        "PROFILE": data.PROFILE,
    }
