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
from pelican_jupyter import markup as nb_markup
from nbconvert.exporters import HTMLExporter
from pathlib import Path
PLUGINS = ["pelican_gist", nb_markup]
MARKUP = ("md", "ipynb")

TYPOGRIFY = False
IPYNB_SKIP_CSS = False
IPYNB_EXPORT_TEMPLATE = str(
    Path(HTMLExporter().template_paths[0]) / "index.html.j2"
)
