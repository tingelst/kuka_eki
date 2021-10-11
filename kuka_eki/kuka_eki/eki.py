# Copyright 2019 Norwegian University of Science and Technology.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Union
from enum import IntEnum
from kuka_eki.tcp_client import Address, TcpClient
from kuka_eki.krl import Axis, Pos, CommandType


class EkiMotionClient:
    MOTION_PORT: int = 54600

    def __init__(self, ip_address: str) -> None:
        self._tcp_client = TcpClient((ip_address, self.MOTION_PORT))

    def connect(self) -> None:
        self._tcp_client.connect()

    def _cmd_xml(
        self,
        cmdtype: int = 0,
        a1: float = 0.0,
        a2: float = 0.0,
        a3: float = 0.0,
        a4: float = 0.0,
        a5: float = 0.0,
        a6: float = 0.0,
        x: float = 0.0,
        y: float = 0.0,
        z: float = 0.0,
        a: float = 0.0,
        b: float = 0.0,
        c: float = 0.0,
        s: int = 0,
        t: int = 0,
        vel: float = 0.0,
    ):
        xml = """<RobotCommand>
  <Type>{cmdtype}</Type>
  <Axis A1="{a1}" A2="{a2}" A3="{a3}" A4="{a4}" A5="{a5}" A6="{a6}"></Axis>
  <Cart X="{x}" Y="{y}" Z="{z}" A="{a}" B="{b}" C="{c}" S="{s}" T="{t}"></Cart>
  <Velocity>{vel}</Velocity>
</RobotCommand>"""
        cmd = xml.format(
            cmdtype=cmdtype,
            a1=a1,
            a2=a2,
            a3=a3,
            a4=a4,
            a5=a5,
            a6=a6,
            x=x,
            y=y,
            z=z,
            a=a,
            b=b,
            c=c,
            s=s,
            t=t,
            vel=vel,
        )
        return cmd

    def ptp(self, cmd: Union[Axis, Pos], max_velocity_scaling=1.0):
        xml: str
        if isinstance(cmd, Axis):
            xml = self._cmd_xml(
                CommandType.PTP_AXIS,
                a1=cmd.a1,
                a2=cmd.a2,
                a3=cmd.a3,
                a4=cmd.a4,
                a5=cmd.a5,
                a6=cmd.a6,
                vel=max_velocity_scaling,
            )
        elif isinstance(cmd, Pos):
            xml = self._cmd_xml(
                CommandType.PTP_CART,
                x=cmd.x,
                y=cmd.y,
                z=cmd.z,
                a=cmd.a,
                b=cmd.b,
                c=cmd.c,
                s=cmd.s,
                t=cmd.t,
                vel=max_velocity_scaling,
            )
        else:
            raise TypeError("Expected argument of type Axis or Pos")
        self._tcp_client.sendall(xml.encode())

    def lin(self, cmd: Pos, max_velocity_scaling=1.0):
        xml: str
        if isinstance(cmd, Pos):
            xml = self._cmd_xml(
                CommandType.LIN_CART,
                x=cmd.x,
                y=cmd.y,
                z=cmd.z,
                a=cmd.a,
                b=cmd.b,
                c=cmd.c,
                vel=max_velocity_scaling,
            )
        else:
            raise TypeError("Expected argument of type Pos")
        self._tcp_client.sendall(xml.encode())


class EkiStateClient:
    STATE_PORT: int = 54601

    def __init__(self, ip_address: str) -> None:
        self._tcp_client = TcpClient((ip_address, self.STATE_PORT))

    def connect(self):
        self._tcp_client.connect()

    def state(self):
        data = self._tcp_client.recv(1024)

        return data
