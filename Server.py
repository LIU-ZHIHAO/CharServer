#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket
import threading
import logging


# Tcp Server
class Charserver(object):
    def __init__(self, ip="192.168.2.101", port=12345):
        self.addr = (ip, port)
        self.sock = socket.socket()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()

        th = threading.Thread(target=self.accept, name="accept")
        th.start()
        th.join()

    def accept(self):
        while True:
            ser, raddr = self.sock.accept()
            print("%s $$$ %s" % (ser, raddr))
            th = threading.Thread(target=self.recve, name="recve", args=(ser, ))
            th.start()
            th.join()

    def recve(self, sock):
        while True:
            data = sock.recv(1024)
            data = data.decode("utf-8")
            print(data)
            # return data to client!
            sock.send(bytes(data.encode("utf-8")))

    def stop(self):
        self.sock.close()


ser1 = Charserver()
ser1.start()
ser1.stop()
