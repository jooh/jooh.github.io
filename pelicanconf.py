#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

IGNORE_FILES = [".ipynb_checkpoints"]
AUTHOR = "Johan Carlin"
SITENAME = "Johan Carlin"
SITEURL = ""
DEFAULT_DATE_FORMAT = "%d %B %Y"
USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE = "fs"
THEME = "./pelican-themes/pelican-bootstrap3"
SHOW_ARTICLE_AUTHOR = True
SHOW_DATE_MODIFIED = True
# could be fun
# SITELOGO = 'TODO.png'
# or BANNER
BOOTSTRAP_THEME = "lumen"
PLUGIN_PATHS = ["./pelican-plugins"]
from pelican_jupyter import markup as nb_markup
PLUGINS = ["pelican_gist", nb_markup, "i18n_subsites", "render_math"]
MARKUP = ("md", "ipynb")
PYGMENTS_STYLE = "solarized-light"
ABOUT_ME = "I am a data engineer based in Stockholm, Sweden. I was once a neuroscientist."
AVATAR = "images/brain.png"
DISPLAY_TAGS_ON_SIDEBAR = False

PATH = "content"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# Blogroll
LINKS = (
    ("code", "https://github.com/jooh"),
    ("rants", "https://twitter.com/johancarlin"),
    ("publications", "https://scholar.google.com/citations?user=hybIdeIAAAAJ"),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# necessary to get ipynb to render properly
# typogrify beaks mathjax
TYPOGRIFY = False
# IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = False

CUSTOM_CSS = 'custom.css'

STATIC_PATHS = ["extra/CNAME", "extra/favicon.ico", "images", "extra/custom.css"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/custom.css": {"path": "custom.css"},
}

