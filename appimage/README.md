# AppImage

This folder contains instruction files for [python-appimage](https://github.com/niess/python-appimage/) to construct an appimage file.

```bash
# (make sure local link is removed)
pip uninstall spydagram

# Ensure inside correct venv environment
cd .. # move to root directory [if running from here]
# Get the appimg python tool
pip install git+https://github.com/niess/python-appimage
# construct ~ req file grabs this directory to build the source version of the package
export APPIMG_RELDIR=$(pwd)
python -m python_appimage build app ./appimage --python-version=3.7
unset APPIMG_RELDIR
# to run
./example_pkg-x86_64.AppImage

# (replace local link)
pip install -e .
```