#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="kuka_eki",
    version="0.0.0",
    description="Control KUKA robots using the Ethernet.KRL interface.",
    author="Lars Tingelstad",
    author_email="lars.tingelstad@ntnu.no",
    license="Apache License 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["kuka_eki"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires=">=3.8",
)
