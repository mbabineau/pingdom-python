
from setuptools import setup

setup(name='pingdom-python',
      version="0.2.1",
      description='Pingdom Library',
      long_description="""3rd-party Python interface to Pingdom's new REST
        API.""",
      author='John Costa',
      author_email='john.costa@gmail.com',
      install_requires=[ 'requests>=0.10.8', 'simplejson'],
      url='https://github.com/johncosta/pingdom-python',
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
