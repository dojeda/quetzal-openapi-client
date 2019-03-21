# coding: utf-8

"""
    Quetzal API

    Quetzal: an API to manage data files and their associated metadata.  # noqa: E501

    OpenAPI spec version: 0.2.0
    Contact: support@quetz.al
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "quetzal-openapi-client"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Quetzal API",
    author_email="support@quetz.al",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Quetzal API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Quetzal: an API to manage data files and their associated metadata.  # noqa: E501
    """
)
