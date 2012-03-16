# -*- coding: utf-8 -*-
"""

    setup
    ~~~~~~~~

    John Costa, 3/16/2012
    License has been consolidated to LICENSE file in root.

    Setup file used for project installation

"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

import pingdom

setup(name='pingdom',
      version=pingdom.__version__,
      description='Pingdom Library',
      long_description="""3rd-party Python interface to Pingdom's new REST
        API. Note that this API is still in beta. See README.rst for
        details""",
      author='Mike Babineau',
      author_email='michael.babineau@gmail.com',
      install_requires=['simplejson'],
      url='http://github.com/EA2D/pingdom-python',
      packages=['pingdom'],
      license='Apache v2.0',
      platforms='Posix; MacOS X; Windows',
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: System Administrators',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: OS Independent',
                   'Topic :: System :: Monitoring', ]
      )
