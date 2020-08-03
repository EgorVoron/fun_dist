import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fun_dist",
    version="0.0.1-beta",
    author="Egor Voron",
    author_email="ekvoron01@gmail.com",
    description="A python package, that provides functions for calculating distances and finding tangents of functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EgorVoron/fun_dist",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
