
import sys
from setuptools import setup

setup(name='pingdom',
      version="0.2.2",
      description='Pingdom Library',
      long_description="""3rd-party Python interface to Pingdom's REST API.""",
      author='Mike Babineau',
      author_email='michael.babineau@gmail.com',
      install_requires=[ 'requests>=0.10.8', 'setuptools>=57.5.0' ],
      url='https://github.com/mbabineau/pingdom-python',
      packages=['pingdom'],
      license='Apache v2.0',
      platforms='Posix; MacOS X; Windows',
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: System Administrators',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: OS Independent',
                   'Topic :: System :: Monitoring', ],
      )
