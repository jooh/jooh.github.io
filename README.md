[![CI](https://github.com/jooh/jooh.github.io/actions/workflows/ci.yml/badge.svg)](https://github.com/jooh/jooh.github.io/actions/workflows/ci.yml)

My personal website.

# Install notes
* This project uses [uv](https://github.com/astral-sh/uv) for Python environments.
  Bootstrap the virtual environment and install dependencies with:
  ```bash
  uv sync
  ```
* When running the Makefile targets with uv, set `USE_UV=1` (for example,
  `make USE_UV=1 html`).
* The dependency list is intentionally broad to support notebooks and site builds.
* [Altair Saver](https://github.com/altair-viz/altair_saver) is *essential* for stopping
  Altair figures from blowing up the webpage size. But conda install is broken as of
  0.5.0 (you get incompatible versions of [some NPM
  dependencies](https://github.com/altair-viz/altair_saver/issues/13#issuecomment-632963608).
  At the moment the workaround is to pip install instead, and then do `npm install -g
  vega-cli vega-lite canvas`. I haven't bothered to include the npm environment spec
  because I expect this to be fixed soon.

# Utilities
* cairosvg is a useful tool for converting Altair SVGs to PDF for keynotes
* nbdime makes it possible to diff notebooks. It should be registered as a git diff
  plugin in the repo.
