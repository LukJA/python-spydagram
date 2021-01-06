Build Procedure
===============

Environment Preparation
-----------------------

This library is designed to work with Python versions >=3.7, this 
must be available in your system path.

Before starting, it is strongly recommended to create a Python3 ``venv`` 
virtual environment (included with Python versions >= 3.3) distinct from your system Python distribution 
to better manage dependencies. This will prevent confusion and allow for
fine control over installed package versions. See `Venv <https://docs.python.org/3/tutorial/venv.html>`_ 
for specifics, but in brief:

.. code-block:: bash

    # - Make a top-level directory
    $ mkdir spydagram-dev
    cd spydagram-dev

    # - Grab the Source
    $ git clone https://github.com/LukJA/python-spydagram.git

    # - Create a new Venv in the top-levek
    $ python3 -m venv .
    # - Activate the venv
    $ source bin/Activate
    # - Check the new Python    - the new `python` default is now 3
    $ python --version            # -> Python 3.7.x

    # - (deactivate the Venv)
    $ deactivate

Dependencies
------------

The library requires ``pycairo`` to generate the output images, which is itself 
dependent on system library ``libcairo2`` and ``pkg-config``. 

Building the library requires the ``libcairo2`` 
development headers: ``libcairo2-dev`` ``libjpeg-dev`` ``libgif-dev`` and python: ``python3-dev``.

In one go, on debian based systems:

.. code-block:: bash

    $ apt-get install libcairo2-dev libjpeg-dev libgif-dev

Python libraries ``setuptools`` and ``wheel`` are required to build the source in preparation for distribution
on PyPI, ``twine`` is needed to upload it to PyPI, and ``Sphinx`` is used to build the ``docs/`` 
documentation files for Read The Docs.

The ``pytest`` library is used for testing purposes.

.. code-block:: bash

    $ pip install pycairo setuptools wheel pytest sphinx # [twine]

Building - Python Library
-------------------------

The Python library is built with ``setuptools`` into an *sdist* and a *wheel*, 
before being sent to PyPI for distribution when the automated CI on github determines a new release
is due. To build with ``setuptools``:

.. code-block:: bash
    
    # - Double check we are in the development Venv
    $ source bin/Activate

    # - Inside python-spydagram/
    # * This will generate ``dist/`` containing the build source and binary libraries
    $ python setup.py sdist bdist_wheel

    # - Upload to test repository using twine
    # python3 -m twine upload --repository testpypi dist/*

Library CLI Mode
^^^^^^^^^^^^^^^^

Python modules can be run explicitly as tools:

.. code-block:: bash

    $ python -m libname --args

This directly runs the contents of a ``__main__.py`` file at the root directory of a library. 
Spydagram [will] function as a CLI script converted, and the above is a valid way of calling
this functionality.

``Setuptools`` has the capability to automatically generate CLI tool execution scripts such that the above 
could equivalently be called by:

.. code-block:: bash

    $ ${tool-libname} --args

These *entry_points* are defined in the setuptools config script ``setup.py``:

.. code-block:: python

    entry_points={
            'console_scripts': [
                'spydagram=spydagram:spydagram_helloWorld',  # entry function => spydagram_helloWorld()
                ],
        },

As soon as ``pip install ${libname}`` is called, ``setuptools`` will also generate and install these *entry_points*.

Building - AppImage
-------------------

Using a Python library or Python tool requires a degree of technical understanding, and a
functional Python binary on the desired system.

To bypass these limitations, we also build an `AppImage <https://appimage.org/>`_, a single file 
executable version of the spydagram library.

The AppImage is essentially a mountable directory containing the library itself, as-well as an 
entire Python distribution provided by `python-appimage <https://github.com/niess/python-appimage>`_.
python-appimage also provides a toolchain to automate the construction of the AppImage, using
a set of instructions found in the projects specific `appimage` directory.

Building the AppImage is fiddly, but is done as follows;

.. code-block:: bash

    # Ensure inside correct venv environment
    $ cd .. # move to root directory [python-spydagram/]
    # Get the appimage Python tool latest from github
    $ pip install git+https://github.com/niess/python-appimage
    # construct ~ requirements file grabs this directory to build the source version of the package
    $ export APPIMG_RELDIR=$(pwd)
    $python -m python_appimage build app ./appimage --python-version=3.7
    $ unset APPIMG_RELDIR
    # to run
    $ ./spydagram-x86_64.AppImage

**entrypoint.sh**

.. literalinclude:: ../../appimage/entrypoint.sh

``entrypoint.sh`` defines what executing the AppImage application will call, in this case we want
it to use the included python ``{{ Python-executable }}`` to run our app in module mode
``-m spydagram``. The call ``"$@"`` tells it to pass any argument we give the AppImage on
to our module.

**requirements.txt**

.. literalinclude:: ../../appimage/requirements.txt

``requirements.txt`` is how we tell python-appimage to install our package into the final executable, 
as well as anything else we want pip to install for any reason. This works just like any pip 
requirements file.

We want to install the raw source files we're working with as a package ``-e /path/to/source``, but 
the directory order of pip and requirements is known to be buggy, so during the build Procedure
we set an environment variable ``export APPIMG_RELDIR=$(pwd)`` so that python-appimage and pip
are able to find our package.

**spydagram.appdata.xml**

.. literalinclude:: ../../appimage/spydagram.appdata.xml

**spydagram.desktop**

.. literalinclude:: ../../appimage/spydagram.desktop




Building - Docs
---------------



Troubleshooting / FAQ
---------------------