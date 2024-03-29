#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket


class CharClient(object):
    def __init__(self, ip="127.0.0.1", port=6787, rip="127.0.0.1", rport=12345):
        self.addr = (ip, port)
        self.saddr = (rip, rport)
        self.sock = socket.socket()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.connect(self.saddr)
        self.sock.send(bytes("this a test!".encode("utf-8")))

    def stop(self):
        self.sock.close()


cli = CharClient()
cli.start()
cli.stop()
