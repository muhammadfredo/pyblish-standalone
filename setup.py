import os
import imp

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()


version_file = os.path.abspath("pyblish_standalone/version.py")
version_mod = imp.load_source("version", version_file)
version = version_mod.version


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities"
]


setup(
    name="pyblish-standalone",
    version=version,
    description="Plug-in driven automation framework for content",
    long_description=readme,
    author="Abstract Factory and Contributors",
    author_email="marcus@abstractfactory.io",
    url="https://github.com/pyblish/pyblish-standalone",
    license="LGPL",
    packages=find_packages(),
    zip_safe=False,
    classifiers=classifiers,
    package_data={"pyblish_standalone": ["plugins/*.py"]},
    install_requires=[
        "pyblish-base>=1.4"
    ],
)
