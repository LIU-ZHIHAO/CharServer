#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket
import multiprocessing

# Tcp Server
class Charserver(object):
    def __init__(self, ip="192.168.2.101", port=12345):
        self.addr = (ip, port)
        self.sock = socket.socket()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()

        p = multiprocessing.Process(target=self.accept, name="accept")
        p.start()

    def accept(self):
        while True:
            ser, raddr = self.sock.accept()
            print("%s $$$ %s" % (ser, raddr))
            p = multiprocessing.Process(target=self.recve, name="recve", args=(ser, ))
            p.start()

    def recve(self, sock):
        while True:
            data = sock.recv(1024)
            data = data.decode()
            print(data)
            # return data to client!
            sock.send(bytes(data.encode()))

    def stop(self):
        self.sock.close()


ser1 = Charserver()
ser1.start()
ser1.stop()
