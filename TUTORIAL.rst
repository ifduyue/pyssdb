pyssdb tutorial
================

Welcome, dear stranger, to a tour de force of ssdb world. Say hello to your
fellow travel companion, the pyssdb client library for Python. You'll get to
know each other fairly well during this trip, so better start off on a friendly
note. And now, let's go!

Getting Started
-----------------

You'll need ssdb listening at default port 8888 to follow along. So simply
start it using: ``ssdb-server ssdb.conf``.

Besides having pyssdb installed, simply run ``pip install pyssdb``.

To use pyssdb we have to import the library and set up a connection to a ssdb
server:

    >>> import pyssdb
    >>> ssdb = pyssdb.Client(host='127.0.0.1', port=8888)

If we leave out the ``host`` and ``port`` parameters, ``'127.0.0.1'`` and
``8888`` would be used as defaults. There is also a ``socket_timeout``
parameter which determines how long, in seconds, the socket will wait for the
server to respond. If it is ``None``, which is the default, the there wil be
no timeout.

Basic Operation
-----------------

Now that we have a connection set up, we can set items:

    >>> ssdb.set('hey!', 'Whoa!')
    1

Or we can get items:

    >>> ssdb.get('hey!')
    'Whoa!'

We can also set items with TTL (time to live), TTL determines how long, in
seconds, an item will exist:

    >>> ssdb.setx('1 second life', 'God, it\'s short!', 1)
    1

If we get this item after one second, we will get ``None``:

    >>> import time
    >>> time.sleep(1)
    >>> ssdb.get('1 second life') is None
    True

