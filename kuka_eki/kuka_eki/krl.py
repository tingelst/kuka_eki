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
from __future__ import annotations
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

    def to_xml(self, root: ET.Element) -> ET.Element:
        element = ET.SubElement(
            root,
            "Axis",
            {
                "A1": str(self.a1),
                "A2": str(self.a2),
                "A3": str(self.a3),
                "A4": str(self.a4),
                "A5": str(self.a5),
                "A6": str(self.a6),
            },
        )
        return element


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

    def to_xml(self, root: ET.Element) -> ET.Element:
        element = ET.SubElement(
            root,
            "Cart",
            {
                "X": str(self.x),
                "Y": str(self.y),
                "Z": str(self.z),
                "A": str(self.a),
                "B": str(self.b),
                "C": str(self.c),
                "S": str(self.s),
                "T": str(self.t),
            },
        )
        return element


class CommandType(IntEnum):
    PTP_AXIS = 1
    PTP_CART = 2
    LIN_CART = 3
    PTP_AXIS_REL = 4
    LIN_CART_REL = 5


@dataclass
class RobotCommand:
    command_type: CommandType
    target: Union[Axis, Pos]
    velocity_scaling: float

    def to_xml(self) -> bytes:
        root = ET.Element("RobotCommand")
        ET.SubElement(root, "Type").text = str(self.command_type.value)
        self.target.to_xml(root)
        Pos().to_xml(root) if isinstance(self.target, Axis) else Axis().to_xml(root)
        ET.SubElement(root, "Velocity").text = str(self.velocity_scaling)
        return ET.tostring(root)


@dataclass
class RobotState:
    axis: Axis = Axis()
    pos: Pos = Pos()

    @classmethod
    def from_xml(cls, xml: bytes) -> RobotState:
        root: ET.Element = ET.fromstring(xml)
        attrib: dict[str, str] = root.find("Pos").attrib
        pos = Pos(
            attrib["X"],
            attrib["Y"],
            attrib["Z"],
            attrib["A"],
            attrib["B"],
            attrib["C"],
            attrib["S"],
            attrib["T"],
        )
        attrib = root.find("Axis").attrib
        axis = Axis(
            attrib["A1"],
            attrib["A2"],
            attrib["A3"],
            attrib["A4"],
            attrib["A5"],
            attrib["A6"],
        )
        return RobotState(axis, pos)

    def to_xml(self) -> bytes:
        root: ET.Element = ET.Element("RobotState")
        self.axis.to_xml(root)
        self.pos.to_xml(root)
        return ET.tostring(root)
