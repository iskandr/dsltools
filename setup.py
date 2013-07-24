#!/usr/bin/env python

from setuptools import setup, Extension

import sys


setup(
    name="TreeLike",
    description="Helpers for creating and traversing recursively nested data structures in Python.", 
    long_description="""
TreeLike
========

Helper classes for creating and traversing recursively nested data structures in Python.  
Useful when simple languages and abstract value domains like type and shape systems. 

""",
    classifiers=['Development Status :: 3 - Alpha',
                 'Topic :: Software Development :: Libraries',
                 'License :: OSI Approved :: BSD License',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python :: 2.7',
                 ],
    author="Alex Rubinsteyn",
    author_email="alexr@cs.nyu.edu",
    license="BSD",
    version="0.2",
    url="http://github.com/iskandr/treelike",
    packages=[ 'treelike'],
    package_dir={ '' : '.' },
    requires=[] 
    )
