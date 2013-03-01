pyssdb
========

Description
-----------
A SSDB Client Library for Python.

Installation
-------------
::

    $ pip install pyssdb --upgrade


Usage
------------
::

    import pyssdb
    c = pyssdb.Client()
    print c.set('key', 'value')
    print c.get('key')
    import string
    for i in string.ascii_letters:
        c.incr(i)
    print c.keys('a', 'z', '10')
    print c.keys('a', 'z', '100')
    print c.get('z')

For the full list of SSDB commands, please check out `this wiki page <https://github.com/ideawu/ssdb/wiki/Commands>`_.
