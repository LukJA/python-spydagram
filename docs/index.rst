python-spydagram
================



Features
-----------

Diagram and scientific sketch .SVG vector image generator, designed to be as fast as free-hand drawing.
Available as a Python library, or as a scripting language and command-line compiler.

[ Code ] -> [ Image ] TBD

Basic Installation
------------------

Install Python library (requires >= python 3.7):

.. code-block:: bash

    pip install spydagram

Use library as such (TBD):

.. code-block:: python

    import spydagram as spy

    sketch = spy.new(spy.graph.2D())
    sketch.print("sketch.svg")

The CLI is included and installed alongside the Python library:

.. code-block:: bash

    spydagram -i "script.txt" -o "sketch.svg"


Alternatively, a pre-packaged `AppImage <https://appimage.org/>`_ version with a Python interpreter included can be obtained from the `releases <https://github.com/LukJA/python-spydagram/releases>`_ page, for systems where a python3 interpreter is not available.

.. code-block:: bash

    ./spydagram-x86_64.AppImage -i "script.txt" -o "sketch.svg"


Note: you may need to make the AppImage file executable on your system.

Contributions
-------------

Contributions are welcome, given the early stage of development please get in touch on the discussions board or via email directly.

* Source Code: `<github.com/LukJA/python-spydagram>`_

License
--------

This projects is licensed under the MIT license, se LICENSE for more details.

.. toctree::
    :maxdepth: 2
    :hidden:
    :numbered:

    source/DeveloperGuide
    source/UserGuide