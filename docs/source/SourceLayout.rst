Source Layout
=============

::

    .
    |-- _spydagram          ## Library Source
    |   |-- _topic              ## Diagrams objects
    |   |-- _primitive          ## Sketches objects
    |   |-- __init__.py         ## Top level library file - holds user objects
    |   \-- __main__.py         ## Module / CLI entry-point
    |
    |-- _test_integ         ## Integration Tests [see testing]
    |   |-- test_main.py
    |   \-- README.md
    |
    |-- _docs               ## Docs Source Code
    |   |-- _source             ## Source files
    |   |   |...
    |   |-- conf.py             ## ReadTheDocs config file
    |   |-- index.rst           ## Documentation home page
    |   |...
    |
    |-- _appimage           ## AppImage generator [see build proc]
    |   |-- entrypoint.sh         ## AppImage shell entry-point
    |   |-- requirements.txt      ## AppImage library installs
    |   |-- spydagram.appdata.xml ## App information
    |   |-- spydagram.desktop     ## Desktop manifest
    |   \-- README.md           
    |   
    |-- _.github/workflows
    |   \-- python-app.yml  ## CI test workflow def
    |
    |-- LICENSE
    |-- .readthedocs.yml    ## ReadTheDocs config fie
    |-- README.md
    \-- setup.py            ## Pip PyPI install config file


Diagrams
--------

Sketches
--------