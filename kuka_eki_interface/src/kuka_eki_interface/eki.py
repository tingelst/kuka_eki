from enum import Enum
from threading import Thread, Lock

from .udp_client import UDPClient
from .krl import Axis, Pos


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
                 x=0.0, y=0.0, z=0.0, a=0.0, b=0.0, c=0.0, s=0, t=0,
                 vel=0.0):
        xml = b'''<RobotCommand>
  <Type>{cmdtype}</Type>
  <Axis A1="{a1}" A2="{a2}" A3="{a3}" A4="{a4}" A5="{a5}" A6="{a6}"></Axis>
  <Cart X="{x}" Y="{y}" Z="{z}" A="{a}" B="{b}" C="{c}" S="{s}" T="{t}"></Cart>
  <Velocity>{vel}</Velocity>
</RobotCommand>'''
        cmd = xml.format(cmdtype=cmdtype,
                         a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6,
                         x=x, y=y, z=z, a=a, b=b, c=c, s=s, t=t,
                         vel=vel)
        return cmd

    def ptp(self, cmd, max_velocity_scaling=1.0):
        if isinstance(cmd, Axis):
            xml = self._cmd_xml(
                CmdType.PTP_AXIS.value,
                a1=cmd.a1,
                a2=cmd.a2,
                a3=cmd.a3,
                a4=cmd.a4,
                a5=cmd.a5,
                a6=cmd.a6,
                vel=max_velocity_scaling)
        elif isinstance(cmd, Pos):
            xml = self._cmd_xml(
                CmdType.PTP_CART.value,
                x=cmd.x,
                y=cmd.y,
                z=cmd.z,
                a=cmd.a,
                b=cmd.b,
                c=cmd.c,
                s=cmd.s,
                t=cmd.t,
                vel=max_velocity_scaling)
        else:
            raise TypeError("Expected argument of type Axis or Pos")
        self._conn.send(xml)

    def lin(self, cmd, max_velocity_scaling=1.0):
        if isinstance(cmd, Pos):
            xml = self._cmd_xml(
                CmdType.LIN_CART.value,
                x=cmd.x,
                y=cmd.y,
                z=cmd.z,
                a=cmd.a,
                b=cmd.b,
                c=cmd.c,
                vel=max_velocity_scaling)
        else:
            raise TypeError("Expected argument of type Pos")
        self._conn.send(xml)

    def start_rsi_axis(self):
        xml = self._cmd_xml(CmdType.RSI_AXIS.value, vel=1.0)
        self._conn.send(xml)
