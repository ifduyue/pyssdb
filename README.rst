pyssdb
======

.. image:: https://travis-ci.org/ifduyue/pyssdb.png
    :target: https://travis-ci.org/ifduyue/pyssdb

.. image:: https://img.shields.io/pypi/v/pyssdb.svg
    :target: https://pypi.python.org/pypi/pyssdb
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/pyssdb.svg
    :target: https://pypi.python.org/pypi/pyssdb
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/l/pyssdb.svg
    :target: https://pypi.python.org/pypi/pyssdb
    :alt: License

pyssdb is an SSDB_ Client Library for Python. SSDB_ is a high
performace key-value(key-string, key-zset, key-hashmap) NoSQL database,
using Google LevelDB as storage engine.

* pyssdb is simple, has no depencencies other than the Python Standard Library.
* pyssdb is pure Python, and is compatible with gevent_.
* pyssdb is thread-safe.

.. _SSDB: https://github.com/ideawu/ssdb
.. _gevent: http://www.gevent.org/

Installation
-------------


.. code-block:: bash

   pip install --upgrade pyssdb


Usage
------------

Here is a short example:

.. code-block:: python

   >>> import pyssdb
   >>> c = pyssdb.Client()
   >>> c.set('key', 'value')
   1
   >>> c.get('key')
   'value'
   >>> c.hset('hash', 'item', 'value')
   1
   >>> c.hget('hash', 'item')
   'value'
   >>> c.hget('hash', 'not exist') is None
   True
   >>> c.incr('counter')
   1
   >>> c.incr('counter')
   2
   >>> c.incr('counter')
   3
   >>> c.keys('a', 'z', 1)
   ['counter']
   >>> c.keys('a', 'z', 10)
   ['counter', 'key']

For more information, see `the tutorial <TUTORIAL.rst>`_, which will explain
most everything.

For the full list of SSDB commands, see
`this page <http://ssdb.io/docs/php/>`_.

License
----------

Copyright (C) 2013-2017 Yue Du, Licensed under
`the 2-clause BSD license <http://opensource.org/licenses/BSD-2-Clause>`_.
