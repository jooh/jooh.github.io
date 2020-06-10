My personal website.

# Install notes
* The conda environment.yml is a bit bloated, but should work with recent python
  notebooks
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
