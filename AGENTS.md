# Repository guide

## Overview
- This repo is a Pelican static site. Source content lives in `content/` with themes in
  `pelican-themes/` and plugins in `pelican-plugins/`.
- Configuration is split between `pelicanconf.py` (local/dev defaults) and
  `publishconf.py` (production settings like `SITEURL` and feeds).
- The generated site is written to the `output/` directory.

## Makefile workflow (main entry point)
- `make html` builds the site from `content/` into `output/` using `pelicanconf.py`.
- `make publish` builds with `publishconf.py` for production output.
- `make serve`, `make devserver`, and `make regenerate` run local rebuild/serve loops.
- `make github` is the deployment path:
  1. Runs `make publish` to generate `output/` using the production config.
  2. Uses `ghp-import` to take the *current source branch state* and write the
     generated `output/` tree into the `master` branch (configured as
     `GITHUB_PAGES_BRANCH`).
  3. Pushes `master` to origin, which is the branch served by GitHub Pages.

## Environment notes
- The repo expects Python tooling and Pelican. If using `uv`, set `USE_UV=1` when
  invoking Makefile targets so commands run via `uv run`.
