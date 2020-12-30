# python-spydagram - [Read The Docs](https://python-spydagram.readthedocs.io/)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/spydagram)
![GitHub](https://img.shields.io/github/license/LukJA/python-spydagram)
![PyPI](https://img.shields.io/pypi/v/spydagram)
![PyPI - Downloads](https://img.shields.io/pypi/dm/spydagram)

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/LukJA/python-spydagram)
[![Documentation Status](https://readthedocs.org/projects/python-spydagram/badge/?version=latest)](https://python-spydagram.readthedocs.io/en/latest/?badge=latest)
![Tests](https://github.com/LukJA/python-spydagram/workflows/System%20Tests/badge.svg?branch=main)

----------

## Features

Diagram and scientific sketch .SVG vector image generator, designed to be as fast as free-hand drawing.
Available as a Python library, or as a scripting language and command-line compiler.

[ Code ] -> [ Image ] TBD

## Basic Installation

Install Python library (requires >= python 3.7):

```bash
pip install spydagram
```

Use library as such (TBD):

```python
import spydagram as spy

sketch = spy.new(spy.graph.2D())
sketch.print("sketch.svg")
```

The CLI is included and installed alongside the Python library:

```bash
spydagram -i "script.txt" -o "sketch.svg"
```

Alternatively, a pre-packaged [AppImage](https://appimage.org/) version with a Python interpreter included can be obtained from the [releases](https://github.com/LukJA/python-spydagram/releases) page, for systems where a python3 interpreter is not available.

```bash
./spydagram-x86_64.AppImage -i "script.txt" -o "sketch.svg"
```

Note: you may need to make the AppImage file executable on your system.

## Contributions

Contributions are welcome, given the early stage of development please get in touch on the discussions board or via email directly.

## License

This projects is licensed under the MIT license, se LICENSE for more details.