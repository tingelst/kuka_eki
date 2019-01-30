from enum import Enum

from .udp_client import UDPClient


class CmdType(Enum):
    PTP_AXIS = 1
    PTP_CART = 2
    LIN_CART = 3
    PTP_AXIS_REL = 4
    LIN_CART_REL = 5
    RSI_AXIS = 6
    RSI_CART = 7


class EKIDriver(object):

    def __init__(self, addr):
        self._conn = UDPClient(addr)


    def start(self):
           self._conn.send(b'0')

    def _cmd_xml(self, cmdtype=0,
                 a1=0.0, a2=0.0, a3=0.0, a4=0.0, a5=0.0, a6=0.0,
                 x=0.0, y=0.0, z=0.0, a=0.0, b=0.0, c=0.0,
                 vel=0.0):
        xml = b'''<RobotCommand>
  <Type>{cmdtype}</Type>
  <Axis A1="{a1}" A2="{a2}" A3="{a3}" A4="{a4}" A5="{a5}" A6="{a6}"></Axis>
  <Cart X="{x}" Y="{y}" Z="{z}" A="{a}" B="{b}" C="{c}"></Cart>
  <Velocity>{vel}</Velocity>
</RobotCommand>'''
        cmd = xml.format(cmdtype=cmdtype,
                         a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6,
                         x=x, y=y, z=z, a=a, b=b, c=c,
                         vel=vel)
        return cmd

    def ptp_axis(self, axis_cmd, max_velocity_scaling=1.0, cont=False):
        xml = self._cmd_xml(
            CmdType.PTP_AXIS.value,
            a1=axis_cmd[0],
            a2=axis_cmd[1],
            a3=axis_cmd[2],
            a4=axis_cmd[3],
            a5=axis_cmd[4],
            a6=axis_cmd[5],
            vel=max_velocity_scaling)
        self._conn.send(xml)

    def ptp_cart(self, cart_cmd, max_velocity_scaling=1.0, cont=False):
        xml = self._cmd_xml(
            CmdType.PTP_CART.value,
            x=cart_cmd[0],
            y=cart_cmd[1],
            z=cart_cmd[2],
            a=cart_cmd[3],
            b=cart_cmd[4],
            c=cart_cmd[5],
            vel=max_velocity_scaling)
        self._conn.send(xml)

    def lin_cart(self, cart_cmd, max_velocity_scaling=1.0, cont=False):
        xml = self._cmd_xml(
            CmdType.LIN_CART.value,
            x=cart_cmd[0],
            y=cart_cmd[1],
            z=cart_cmd[2],
            a=cart_cmd[3],
            b=cart_cmd[4],
            c=cart_cmd[5],
            vel=max_velocity_scaling)
        self._conn.send(xml)

    def ptp_axis_rel(self, rel_axis_cmd, max_velocity_scaling=1.0, cont=False):
        xml = self._cmd_xml(
            CmdType.PTP_AXIS_REL.value,
            a1=rel_axis_cmd[0],
            a2=rel_axis_cmd[1],
            a3=rel_axis_cmd[2],
            a4=rel_axis_cmd[3],
            a5=rel_axis_cmd[4],
            a6=rel_axis_cmd[5],
            vel=max_velocity_scaling)
        self._conn.send(xml)

    def lin_cart_rel(self, rel_cart_cmd, max_velocity_scaling=1.0, cont=False):
        xml = self._cmd_xml(
            CmdType.LIN_CART_REL.value,
            x=rel_cart_cmd[0],
            y=rel_cart_cmd[1],
            z=rel_cart_cmd[2],
            a=rel_cart_cmd[3],
            b=rel_cart_cmd[4],
            c=rel_cart_cmd[5],
            vel=max_velocity_scaling)
        self._conn.send(xml)

    def rsi_axis(self,):
        xml = self._cmd_xml(CmdType.RSI_AXIS.value)
        self._conn.send(xml)

    def rsi_cart(self,):
        xml = self._cmd_xml(CmdType.RSI_CART.value)
        self._conn.send(xml)
