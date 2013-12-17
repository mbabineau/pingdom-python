==============
pingdom-python
==============
3rd-party Python library for Pingdom_.'s new REST API.
Note that this API is still in beta, so may change at any time.  For more
information about the API, see Pingdom's blog post_.

Currently, the library supports:

* Checks (create, delete, get, list)

============
Requirements
============

- Pingdom account
- requests (0.10.8 or newer)

=============
Documentation
=============

More project documentation can be found in the docs directory. Documentation
can be built using sphinx.

    pip install sphinx

    cd docs

    make html

.. _Pingdom: http://pingdom.com
.. _post: http://royal.pingdom.com/2011/03/22/new-pingdom-api-enters-public-beta/