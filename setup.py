import os
from setuptools import setup, find_packages
from pathlib import Path

long_description = """
Ansible Semaphore API

API Python Client allows communication with Ansible-Semaphore API.

API demo: https://www.ansible-semaphore.com/api-docs/

Docs: https://github.com/nchekwa/ansible-semaphore-api

This Package is Auto-Generated based on API-Docs from Ansible-Semaphore.
 
"""

NAME = os.getenv('PYPI_NAME', "semaphore_api")   
VERSION = os.getenv('PYPI_VERSION', os.getenv('SEMAPHORE_VERSION', "0.0.1a"))

setup(
    name=NAME,
    version=VERSION,
    description="Ansible Semaphore Python API",
    author="Nchekwa",
    author_email="artur@nchekwa.com",
    url="https://github.com/nchekwa/ansible-semaphore-api",
    keywords=["ansible-semaphore", "semaphore", "ansible", "api"],
    install_requires=[ "python_dateutil >= 2.5.3", "setuptools >= 21.0.0", "urllib3 >= 1.25.3, < 2.1.0", "pydantic >= 2", "typing-extensions >= 4.7.1" ],
    packages=find_packages(exclude=["test", "tests", "docs"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    package_data = {NAME: ['py.typed']}
)
