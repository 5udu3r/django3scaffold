#!/usr/bin/env python

from __future__ import absolute_import
try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test

from django3scaffold import settings

import os

here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here,  'README.RST'))
long_description = f.read().strip()
f.close()


setup(
    name='django3scaffold',
    version=settings.VERSION,
    author='Tokyo Developers',
    author_email='admin@tokyodevs.com',
    url='https://github.com/tokyodevs/django3scaffold',
    description = 'Faster Development For Django 3 Projects',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='django',
    zip_safe=False,
    install_requires=[
        'Django>=3.0',
        'South>=0.7.2',
        'simplejson>=3.17.0',
    ],
    test_suite = 'django3scaffold.tests',
    include_package_data=True,
    # cmdclass={},
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
