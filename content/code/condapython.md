Title: Reproducible scientific python setup with (Ana) Conda
Tags: python, data science, conda, anaconda, scientific computing, virtual environment
Date: 2015-12-11

Getting a scientific python install up and running is still way too
complicated. In this post I describe how I use a conda to keep a
reproducible record of the packages I use.

In the past, I have usually hacked together my own developing environment
through whatever tools were most convenient (pip, github clones, built-in
packages from expansive standard python distros). This is a workable
solution if you're only doing it once, but it can be quite challenge to
achieve the exact same python environment on a new machine. This is
annoying in lots of contexts, but it's especially problematic for
scientific computing because it means others (or even your future self) may
not be able to reproduce your published results.

My solution to this issue is to use
[Conda](http://conda.pydata.org/docs/index.html), which forms an
independent part of the Anaconda python distro (I use the lighter
mini-conda). At its core, Conda is a package manager which tries to be
smart about managing your python environment. There are many competitors in
this area (the classic solution is pip combined with virtualenv, brew and
macports are other possibilities), but Conda has a few useful features that
collectively make it preferable for scientific computing:

* Conda packages are distributed in compiled form, which avoids all
  build-related issues (e.g., missing dependencies, broken compilers, weird
  build environments). If the package has been built properly, it is
  literally plug and play. For a taste of how smoothly this works with
  complex packages, try `conda install mayavi` compared to `brew install
  mayavi` and see what you get.
* If a conda package is not available, it is surprisingly easy to build one
  from python libraries.  Most pip packages can be built for conda with two
  commands: `conda skeleton pypi [pip package]` followed by `conda build
  [pip package]`.  Adapting github repos requires a bit more manual
  editing of a YAML file but even this is simple enough (see e.g. [this
  pycortex recipe I
  wrote](https://github.com/jooh/neuroconda/tree/master/pycortex)). Under
  the hood, there's quite a bit of cleverness going on with e.g. converting
  absolute paths to relative to enable this to work as smoothly as it does.
* Conda includes a free package repository at
  [anaconda.org](http://anaconda.org), where users can upload packages.
  At build time, users are nudged toward setting `anaconda_upload: yes` in
  their .condarc files, which means that any successful build is
  uploaded to your anaconda.org repo. This option appears to be popular
  because a huge number of user-built packages are available here. This is
  useful for quickly checking out more obscure packages that aren't in
  the official conda channel.
* That being said, for reproducibility it is probably a better idea to
  build packages yourself and upload them to your own repository since
  other users can otherwise break your dependencies by removing or altering
  the package you're channeling. Uploading your own builds has the added
  advantage of solving your deployment issues -- all you have to do on a new
  machine is add your repository to the set conda will search when
  installing packages (e.g., `conda config --add channels jcarlin`), and
  the standard conda install command will just work.
* Conda's environment handling is quite good, and seems to err on the side
  of safety at the expense of disk space (ie, copy everything) compared to
  e.g. brew. I have yet to bump into any interactions between different
  environments. Generally, it's a good idea to have a different environment
  for each broad task you use python for (I use one for psychopy, one for
  neuroimaging analysis and one for web development), since packages
  sometimes require different versions of the same modules. Conda tries to
  manage such situations, but often the compromise is to downgrade core
  packages (e.g. numpy) to fairly old versions.

In summary, my entire python environment is now made up of Conda packages,
which is neat because it means that I can reproduce my python setup
anywhere. There is a bit of overhead in going this route (especially if you
want to avoid having dependencies from other anaconda.org users), but this
should be recouped quickly down the road as the code gets deployed to
psychophysics test laptops, cloud compute, other lab members...
