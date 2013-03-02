#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
pyssdb
~~~~~~~

A SSDB Client Library for Python.

:copyright: (c) 2013 by Yue Du.
:license: BSD 2-clause License, see LICENSE for more details.
'''

__version__ = '0.0.1'
__author__ = 'Yue Du <ifduyue@gmail.com>'
__url__ = 'https://github.com/ifduyue/pyssdb'
__license__ = 'BSD 2-Clause License'

import socket
import functools

class error(Exception):
    def __init__(self, reason, *args):
        super(error, self).__init__(reason, *args)
        self.reason = reason
        self.message = ' '.join(args)

class Client(object):
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port
        self.connect()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.fp = self.socket.makefile('rb')

    def close(self):
        try:
            self.socket.close()
        except socket.error:
            pass

    def reconnect(self):
        self.close()
        self.connect()

    def _send(self, cmd, *args):
        if cmd == 'delete':
            cmd = 'del'
        args = (cmd, ) + args
        buf = ''.join('%d\n%s\n' % (len(i), i) for i in args) + '\n'
        self.socket.sendall(buf)
        return_list = 'keys' in cmd or 'scan' in cmd or 'list' in cmd
        return self._recv(return_list)

    def _recv(self, return_list=False):
        ret = []
        while True:
            line = self.fp.readline().rstrip('\n')
            if not line:
                break
            data = self.fp.read(int(line))
            self.fp.read(1) # discard '\n'
            ret.append(data)
        if ret[0] == 'not_found':
            return None
        if ret[0] == 'ok':
            ret = ret[1:]
            if return_list:
                return ret
            if not ret:
                return None
            if len(ret) == 1:
                return ret[0]
        raise error(*ret)

    def __getattr__(self, cmd):
        if cmd in self.__dict__:
            return self.__dict__[cmd]
        elif cmd in self.__class__.__dict__:
            return self.__class__.__dict__[cmd]
        ret = self.__dict__[cmd] = functools.partial(self._send, cmd)
        return ret

if __name__ == '__main__':
    c = Client()
    print c.set('key', 'value')
    print c.get('key')
    import string
    for i in string.ascii_letters:
        c.incr(i)
    print c.keys('a', 'z', '10')
    print c.keys('a', 'z', '100')
    print c.get('z')
