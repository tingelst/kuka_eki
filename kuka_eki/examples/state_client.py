# Copyright 2021 Norwegian University of Science and Technology.
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
from kuka_eki.eki import EkiMotionClient 
from kuka_eki.krl import Pos, Axis
from kuka_eki.tcp_client import TcpClient


target = Axis(0.0, -90.0, 90.0, 0.0, 0.0, 0.0)

eki_state_client = TcpClient(("192.168.250.20", 54601))

eki_state_client.connect()

while True:
    data = eki_state_client.recv(1024)
    print(data)

# eki_motion_client.connect()

# eki_motion_client.ptp(target)


