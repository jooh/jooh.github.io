from pathlib import Path

from nbconvert.exporters import HTMLExporter
from pelican_jupyter import markup as nb_markup

AUTHOR = "Test"
SITENAME = "Test Site"
SITEURL = ""

PATH = "content"
OUTPUT_PATH = "output"

TIMEZONE = "UTC"
DEFAULT_LANG = "en"

THEME = "simple"
RELATIVE_URLS = True

PLUGIN_PATHS = ["./pelican-plugins"]
PLUGINS = ["pelican_gist", nb_markup]
MARKUP = ("md", "ipynb")

TYPOGRIFY = False
IPYNB_SKIP_CSS = False
IPYNB_EXPORT_TEMPLATE = str(Path(HTMLExporter().template_paths[0]) / "index.html.j2")
