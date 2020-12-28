import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spydagram", # Replace with your own username
    version="0.0.1.dev1",
    author="Luke Andrews",
    author_email="l.j.andrews.uk@gmail.com",
    description="Spyda Placeholder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LukJA/python-spydagram",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)