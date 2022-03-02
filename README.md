<!--
    =====================================
    generator=datazen
    version=1.13.3
    hash=d7b6e8b69a63ccb83dd35cc31c31c068
    =====================================
-->

# svgen ([0.2.0](https://pypi.org/project/svgen/))

[![python](https://img.shields.io/pypi/pyversions/svgen.svg)](https://pypi.org/project/svgen/)
![Build Status](https://github.com/vkottler/svgen/workflows/Python%20package/badge.svg)
[![codecov](https://codecov.io/gh/vkottler/svgen/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/github/vkottler/svgen)

*A tool for working with scalable vector graphics.*

# Command-line Options

```
$ ./venv3.8/bin/svgen -h

usage: svgen [-h] [--version] [-v] [-C DIR] [-c CONFIG] [-o OUTPUT] script

A tool for working with scalable vector graphics.

positional arguments:
  script                script to run for composing the SVG document

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         set to increase logging verbosity
  -C DIR, --dir DIR     execute from a specific directory
  -c CONFIG, --config CONFIG
                        top-level configuration to load (default:
                        'svgen.json')
  -o OUTPUT, --output OUTPUT
                        file to write SVG output (default: 'svgen.svg')

```
