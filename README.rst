pyssdb
========

pyssdb is a SSDB_ Client Library for Python. SSDB_ is a high
performace key-value(key-string, key-zset, key-hashmap) NoSQL database,
using Google LevelDB as storage engine.

* pyssdb is simple, has no depencencies other than the Python Standard Library.
* pyssdb is pure Python, and is compatible with gevent_.
* pyssdb is thread-safe.

.. _SSDB: https://github.com/ideawu/ssdb
.. _gevent: http://www.gevent.org/

Installation
-------------
::

    $ pip install pyssdb --upgrade


Usage
------------

Here is a short example::

    import pyssdb
    c = pyssdb.Client()
    print c.set('key', 'value')
    print c.get('key')
    import string
    for i in string.ascii_letters:
        c.incr(i)
    print c.keys('a', 'z', 1)
    print c.keys('a', 'z', 10)
    print c.get('z')

For the full list of SSDB commands, check out
`this wiki page <https://github.com/ideawu/ssdb/wiki/Commands>`_.

License
----------

Copyright (C) 2013-2014 Yue Du, Licensed under
`the 2-clause BSD license <http://opensource.org/licenses/BSD-2-Clause>`_.

