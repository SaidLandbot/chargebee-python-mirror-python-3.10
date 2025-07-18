# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "chargebee"))
if sys.version_info < (3, 10):
    sys.exit("Sorry, Python < 3.10 is not supported")
from chargebee.version import VERSION

with open("README.md", "r") as file:
    description = file.read()

requires = ["requests"]

setup(
    name="chargebee-mirror",
    version=VERSION,
    author="Landbot",
    author_email="said.a@landbot.io",
    url="https://apidocs.chargebee.com/docs/api?lang=python",
    description="Python wrapper for the Chargebee Subscription Billing API",
    packages=find_packages(exclude=["tests"]),
    package_data={"chargebee": ["ssl/*.crt"]},
    python_requires=">=3.10",
    install_requires=requires,
    test_suite="tests",
    long_description=description,
    long_description_content_type="text/markdown",
)
