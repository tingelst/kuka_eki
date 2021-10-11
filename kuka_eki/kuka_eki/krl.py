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
from dataclasses import dataclass
from enum import IntEnum
import xml.etree.ElementTree as ET


@dataclass
class Axis:
    a1: float = 0.0
    a2: float = 0.0
    a3: float = 0.0
    a4: float = 0.0
    a5: float = 0.0
    a6: float = 0.0

    def to_xml(self):
        xml = (
            "<Axis "
            f'A1="{self.a1}" A2="{self.a2}" A3="{self.a3}"'
            f'A4="{self.a4}" A5="{self.a5}" A6="{self.a6}"'
            "</Axis>"
        )
        return xml


@dataclass
class Pos:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    a: float = 0.0
    b: float = 0.0
    c: float = 0.0
    s: int = 0
    t: int = 0

    def to_xml(self):
        xml = (
            "<Cart"
            f'X="{self.x}" Y="{self.y}" Z="{self.z}"'
            f'A="{self.a}" B="{self.b}" C="{self.c}"'
            f'S="{self.s}" T="{self.t}">'
            "</Cart>"
        )
        return xml


class CommandType(IntEnum):
    PTP_AXIS = 1
    PTP_CART = 2
    LIN_CART = 3
    PTP_AXIS_REL = 4
    LIN_CART_REL = 5


@dataclass
class RobotCommand:
    command_type: CommandType
    command: Union[Axis, Pos]
    velocity_scaling: float

    def to_xml(self):
        root = ET.Element("RobotCommand")
        ET.SubElement(root, "Type").text = str(1)

        ET.SubElement(
            root,
            "Pos",
            {"X": str(0.0), "Y": "0.0", "Z": "0.0", "A": "0.0", "B": "0.0", "C": "0.0"},
        )
        return ET.tostring(root)

        xml = "<RobotCommand>"
        xml += f"<Type>{self.command_type}</Type>"
        if isinstance(self.command, Axis):
            xml += self.command.to_xml()
            xml += Pos().to_xml()
        elif isinstance(self.command, Pos):
            xml += Axis().to_xml()
            xml += self.command.to_xml()
        else:
            raise TypeError("Expected argument of type Axis or Pos")
        xml += f"<Velocity>{self.velocity_scaling}</Velocity>"
        xml += "</RobotCommand>"
        return xml


@dataclass
class RobotState:
    axis: Axis
    pos: Pos

    @classmethod
    def from_bytes(cls, bytes_: bytes):
        pass


if __name__ == "__main__":

    cmdtype = CommandType.PTP_AXIS
    cmd = Axis(1, 2, 3, 4, 5, 6)

    cmd = Pos(1, 2, 3, 4, 5, 6, 7, 8)
    vel = 1.0

    s = RobotCommand(cmdtype, cmd, vel)
