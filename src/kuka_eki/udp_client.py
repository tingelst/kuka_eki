from enum import Enum
import socket

class CmdType(Enum):
    PTP_AXIS = 1
    PTP_CART = 2
    LIN_CART = 3
    PTP_AXIS_REL = 4
    LIN_CART_REL = 5
    RSI = 6

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
