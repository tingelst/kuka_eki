from enum import Enum
import socket

class UDPClient:
    def __init__(self, addr):
        self._addr = addr
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def sendall(self, data):
        self._socket.sendall(data)

    def send(self, data):
        return self._socket.sendto(data, self._addr)

    def recv(self, size):
        data, addr = self._socket.recvfrom(size)
        return data

    def __del__(self):
        self._socket.close()
