
import sys
from setuptools import setup

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='pingdom',
      version="0.2.0",
      description='Pingdom Library',
      long_description="""3rd-party Python interface to Pingdom's REST API.""",
      author='Mike Babineau',
      author_email='michael.babineau@gmail.com',
      install_requires=[ 'requests>=0.10.8' ],
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
      **extra
      )
