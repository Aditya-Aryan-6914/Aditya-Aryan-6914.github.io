from django import template
from django.conf import settings
from django.urls import reverse

register = template.Library()


@register.simple_tag
def link(name, *args):
    """Site-relative URL honouring BASE_PATH (for project pages on GitHub Pages)."""
    return settings.SITE["base_path"] + reverse(name, args=args)


@register.simple_tag
def asset(path):
    return f"{settings.SITE['base_path']}/static/{path}"


@register.simple_tag
def absolute(name, *args):
    return settings.SITE["url"] + reverse(name, args=args)


@register.filter
def initials(name):
    return "".join(w[0] for w in name.split()[:2]).upper()
