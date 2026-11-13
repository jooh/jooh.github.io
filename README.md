[![CI](https://github.com/jooh/jooh.github.io/actions/workflows/ci.yml/badge.svg)](https://github.com/jooh/jooh.github.io/actions/workflows/ci.yml)
[![CD](https://github.com/jooh/jooh.github.io/actions/workflows/cd.yml/badge.svg)](https://github.com/jooh/jooh.github.io/actions/workflows/cd.yml)

My personal website.

Mermaid diagrams use standard fenced Markdown blocks with the `mermaid` language.
The Markdown build preserves them for the browser renderer. Pages containing a
diagram load the vendored Mermaid 12.3.0 browser bundle from the site itself.
Rendering requires JavaScript. Pelican copies the bundle as static files, so a
site build needs only the existing Python toolchain.

To update Mermaid, download the pinned `mermaid` package from the npm registry
and verify the tarball against its `dist.integrity` value. Copy `LICENSE`,
`dist/mermaid.esm.min.mjs`, and all `.mjs` files under
`dist/chunks/mermaid.esm.min/` into a new version directory under
`content/extra/vendor/mermaid/`. Keep the `chunks/mermaid.esm.min/` layout next
to the entry module so Mermaid can load diagram types on demand. Update the
version in the template, integration test, and this README, and remove the old
version directory.

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
