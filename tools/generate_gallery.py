#!/usr/bin/env python3
"""
Generate thumbnail images and a `Images/gallery.json` manifest for the gallery.

Usage:
  python3 tools/generate_gallery.py

Requirements:
  pip install pillow

This script looks for images in the `Images/` folder (jpg/png/webp). It skips
`Logo.png` and `PHOTO.jpg` by default. Thumbnails are written to `Images/thumbs/`.
A JSON manifest `Images/gallery.json` is written containing objects with `src`,
`thumb`, and `alt` fields.
"""
import os
import json
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(__file__))
IMAGES_DIR = os.path.join(ROOT, 'Images')
THUMBS_DIR = os.path.join(IMAGES_DIR, 'thumbs')
MANIFEST = os.path.join(IMAGES_DIR, 'gallery.json')

EXCLUDE = {'Logo.png', 'PHOTO.jpg'}
ALLOWED_EXT = {'.jpg', '.jpeg', '.png', '.webp'}

os.makedirs(THUMBS_DIR, exist_ok=True)

entries = []
for name in sorted(os.listdir(IMAGES_DIR)):
    if name in EXCLUDE:
        continue
    src = os.path.join(IMAGES_DIR, name)
    if not os.path.isfile(src):
        continue
    root, ext = os.path.splitext(name)
    if ext.lower() not in ALLOWED_EXT:
        continue

    try:
        im = Image.open(src)
    except Exception as e:
        print(f"Skipping {name}: cannot open ({e})")
        continue

    # create thumbnail
    thumb_w = 800 if im.width > 1200 else 480
    im.thumbnail((thumb_w, thumb_w), Image.LANCZOS)
    thumb_name = f"thumb_{name}"
    thumb_path = os.path.join(THUMBS_DIR, thumb_name)
    im.save(thumb_path, quality=85)

    entries.append({
        'src': f'Images/{name}',
        'thumb': f'Images/thumbs/{thumb_name}',
        'alt': root.replace('-', ' ').replace('_', ' ')
    })

with open(MANIFEST, 'w', encoding='utf8') as f:
    json.dump(entries, f, indent=2)

print(f"Wrote {len(entries)} images to {MANIFEST}")
