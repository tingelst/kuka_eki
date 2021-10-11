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

@dataclass
class Axis:
    a1: float
    a2: float
    a3: float
    a4: float
    a5: float
    a6: float


@dataclass
class Pos:
    x: float
    y: float
    z: float
    a: float
    b: float
    c: float
    s: float
    t: float

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
