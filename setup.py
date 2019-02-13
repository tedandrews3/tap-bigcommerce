#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-bigcommerce",
    version="0.1.0",
    description="Sync data from your BigCommerce Store",
    author="Chris Goddard",
    url="https://github.com/chrisgoddard",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_bigcommerce"],
    install_requires=[
        "singer-python==5.0.12",
        "requests==2.21.0"
    ],
    entry_points="""
    [console_scripts]
    tap-bigcommerce=tap_bigcommerce:main
    """,
    packages=["tap_bigcommerce"],
    package_data = {
        "schemas": ["tap_bigcommerce/schemas/*.json"]
    },
    include_package_data=True,
)