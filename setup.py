#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='falcon-generic-handler',
    version='0.0.1',
    description=u'',
    author='Jeongsoo Park',
    author_email='toracle@gmail.com',
    url='https://github.com/toracle/falcon-generic-handler',
    packages=[
        'falcon_generic_handler',
    ],
    install_requires=[
        'falcon',
        'simplejson',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Falcon',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
)
