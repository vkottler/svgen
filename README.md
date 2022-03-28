<!--
    =====================================
    generator=datazen
    version=1.14.0
    hash=ec38be764cda38772fe1d4919c8a73ff
    =====================================
-->

# svgen ([0.2.1](https://pypi.org/project/svgen/))

[![python](https://img.shields.io/pypi/pyversions/svgen.svg)](https://pypi.org/project/svgen/)
![Build Status](https://github.com/vkottler/svgen/workflows/Python%20package/badge.svg)
[![codecov](https://codecov.io/gh/vkottler/svgen/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/github/vkottler/svgen)

*A tool for working with scalable vector graphics.*

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
