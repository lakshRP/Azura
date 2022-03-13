# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'venv/README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="azura",
    version="0.1.1",
    description="Azura is an add-on to the math library. It contains many functions and 2 sub-libraries (percents and geography). In the sub-library, you can calculate percent proportions. In the sub-library you can use the Haversine function with distancetype conversions. In the built-in functions you can use geometric functions and also you can refer to pi, e, tau. In the built-in library some functions will have a perimeter, simplification. You can put 's' for pi to be converted to 3.14. Otherwise, if you want the normal pi, simply put any other string. Made by Laksh Patel, cannot be distributed as your own.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Laksh Patel",
    author_email="laksh2008patel@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["azura"],
    include_package_data=True,
    install_requires=["numpy"]
)