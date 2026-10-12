---
title: "How to Deploy a Django Project on PythonAnywhere (Free Tier, Step by Step)"
date: 2026-09-20
category: Django
tags: [django, deployment, pythonanywhere, python]
description: "A beginner-friendly walkthrough for deploying a Django app to PythonAnywhere: virtualenv, WSGI file, static files, ALLOWED_HOSTS and the mistakes that cause a blank error page."
---

Running `python manage.py runserver` on your laptop is easy. Getting the same project onto a public URL is where most students get stuck. PythonAnywhere is one of the friendliest places to do it because it is built for Python and has a free tier. This guide walks through the full process, including the small settings that usually cause the dreaded error page.

## What you need before you start

- A Django project that already works locally.
- The project pushed to a GitHub repository.
- A free PythonAnywhere account. Your site will live at `yourusername.pythonanywhere.com`.
- A `requirements.txt` file. If you do not have one, run `pip freeze > requirements.txt` inside your local virtual environment and commit it.

## Step 1: Get your code onto PythonAnywhere

Open a **Bash console** from the PythonAnywhere dashboard and clone your repository:

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

## Step 2: Create a virtual environment

Pick the same Python version your project uses locally, then install the dependencies:

```bash
mkvirtualenv --python=/usr/bin/python3.12 myenv
pip install -r requirements.txt
```

Note the virtualenv name. You will paste its path into the Web tab shortly.

## Step 3: Create the web app

1. Go to the **Web** tab and click **Add a new web app**.
2. Choose **Manual configuration** (not the "Django" wizard) and select your Python version.
3. In the **Virtualenv** section enter `/home/yourusername/.virtualenvs/myenv`.
4. Under **Code**, set the source directory to the folder that contains `manage.py`.

## Step 4: Edit the WSGI file

Click the WSGI configuration file link on the Web tab. Delete the default content and point it at your project:

```python
import os
import sys

path = "/home/yourusername/your-project"
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Replace `config.settings` with the real name of your settings module, which is the folder that holds `settings.py`.

## Step 5: Fix `settings.py` for production

Three settings matter most:

```python
DEBUG = False
ALLOWED_HOSTS = ["yourusername.pythonanywhere.com"]
STATIC_ROOT = BASE_DIR / "staticfiles"
```

If `ALLOWED_HOSTS` is wrong you will see a `400 Bad Request` page. Never leave `DEBUG = True` on a public site because it can expose your settings and source paths in error pages.

## Step 6: Static files

Django does not serve CSS and JavaScript on its own in production. In the Bash console run:

```bash
python manage.py collectstatic
python manage.py migrate
```

Then, on the Web tab under **Static files**, add a mapping:

| URL | Directory |
| --- | --- |
| `/static/` | `/home/yourusername/your-project/staticfiles` |

## Step 7: Reload and test

Press the green **Reload** button on the Web tab and visit your URL. If something is wrong, open the **error log** link on the same tab. The last few lines almost always tell you exactly what failed.

## Common mistakes and fixes

- **ImportError: No module named ...** means the virtualenv path on the Web tab is wrong, or you forgot to `pip install` inside it.
- **Site loads without styling** means the static files mapping is missing, or you did not run `collectstatic`.
- **DisallowedHost error** means your domain is missing from `ALLOWED_HOSTS`.
- **Changes do not show up** usually means you did not `git pull` and press Reload after pushing new code.

## Keep your secrets out of Git

Do not commit your `SECRET_KEY`. Read it from an environment variable instead, and set that variable in the WSGI file or a `.env` file that is listed in `.gitignore`.

## Wrapping up

Once you have deployed one project, the process becomes routine: clone, virtualenv, WSGI, static files, reload. Keep a short checklist and the next deployment will take minutes instead of an afternoon. If a step in this guide does not match what you see, PythonAnywhere's interface changes occasionally, so check their help pages and tell me through the contact page so I can update this post.
