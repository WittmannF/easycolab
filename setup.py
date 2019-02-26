#! /usr/bin/env python
#
# Copyright (C) 2019 Fernando Marcos Wittmann


VERSION = '0.1b24'

SHORT_DESCRIPTION = "EasyColab: Easy access to the most used methods on Google Colab"

LONG_DESCRIPTION = """\
Easy to use tools to be used on Google Colab. This Python package implements some of the most useful commands such as mounting Google drive folders, download of big files and zip/unzip files.

## How to install
1. Open a Google Colab Session.
2. On a new cell, type:
```
!pip install easycolab
```
3. Try importing easycolab to check if the installation worked:
```
import easycolab as ec
```

"""

DISTNAME = 'easycolab'
AUTHOR = 'Fernando Marcos Wittmann'
AUTHOR_EMAIL = 'fernando.wittmann@gmail.com'
DOWNLOAD_URL = 'https://github.com/wittmannf/easycolab/'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

def check_dependencies():
    install_requires = []
    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            "Programming Language :: Python :: 2",
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
        description=SHORT_DESCRIPTION,
        install_requires=install_requires,
        license="MIT",
        long_description=LONG_DESCRIPTION,
        include_package_data=True,
        keywords='easycolab',
        name='easycolab',
        packages=['easycolab'],
        url=DOWNLOAD_URL,
        version=VERSION,
        zip_safe=False,
    )
