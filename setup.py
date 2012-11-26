#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="google-protobuf",
    url="http://www.flyzen.com",
    license="BSD",
    author="Young King",
    author_email="yanckin@google.com",
    description="",
    version="0.2",
    packages=find_packages('.'),
    namespace_packages=['google'],
    package_dir={'': '.'},
)
