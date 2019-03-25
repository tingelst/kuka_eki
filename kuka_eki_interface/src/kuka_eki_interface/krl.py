# Copyright (c) 2019 Norwegian University of Science and Technology
# Use of this source code is governed by the BSD 3-Clause license, see LICENSE
#
# Author: Lars Tingelstad


class Axis(object):
    def __init__(self):
        self.a1 = 0.0
        self.a2 = 0.0
        self.a3 = 0.0
        self.a4 = 0.0
        self.a5 = 0.0
        self.a6 = 0.0

    def tolist(self):
        return [self.a1, self.a2, self.a3, self.a4, self.a5, self.a6]


class Pos(object):
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.s = 0
        self.t = 0

    def tolist(self):
        return [self.x, self.y, self.z, self.a, self.b, self.c, self.s, self.t]
