<!--
    =====================================
    generator=datazen
    version=2.1.0
    hash=c7c7f107196cafc61a3d53cbe16f04a4
    =====================================
-->

# svgen ([0.2.3](https://pypi.org/project/svgen/))

[![python](https://img.shields.io/pypi/pyversions/svgen.svg)](https://pypi.org/project/svgen/)
![Build Status](https://github.com/vkottler/svgen/workflows/Python%20Package/badge.svg)
[![codecov](https://codecov.io/gh/vkottler/svgen/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/github/vkottler/svgen)

*A tool for working with scalable vector graphics.*

See also: [generated documentation](https://vkottler.github.io/python/pydoc/svgen.html)
(created with [`pydoc`](https://docs.python.org/3/library/pydoc.html)).

# Command-line Options

```
$ ./venv3.8/bin/svgen -h

usage: svgen [-h] [--version] [-v] [-C DIR] [-c CONFIG] [--height HEIGHT]
             [--width WIDTH] [-o OUTPUT]
             [scripts [scripts ...]]

A tool for working with scalable vector graphics.

positional arguments:
  scripts               scripts to run for composing the SVG document (in
                        order)

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         set to increase logging verbosity
  -C DIR, --dir DIR     execute from a specific directory
  -c CONFIG, --config CONFIG
                        top-level configuration to load (default:
                        'svgen.json')
  --height HEIGHT       height of the document, if not specified by
                        configuration (default: 100)
  --width WIDTH         width of the document, if not specified by
                        configuration (default: 100)
  -o OUTPUT, --output OUTPUT
                        file to write SVG output (default: 'svgen.svg')

```

# Internal Dependency Graph

A coarse view of the internal structure and scale of
`svgen`'s source.
Generated using [pydeps](https://github.com/thebjorn/pydeps) (via
`mk python-deps`).

![svgen's Dependency Graph](im/pydeps.svg)
