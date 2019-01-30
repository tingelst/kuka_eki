
# coding: utf-8

# In[125]:


from krc_handler import AbstractRobot, KRC4
import math3d
import numpy as np
np.set_printoptions(suppress=True)
import socket
import xml.etree.ElementTree as ET
import ipywidgets as widgets
from IPython.display import display


# In[126]:


from enum import Enum


# In[2]:


class TCPClient:
    def __init__(self, host, port):
        self._host = host
        self._port = port

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self._host, self._port))

    def sendall(self, data):
        self._socket.sendall(data)
        
    def send(self, data):
        return self._socket.send(data)

    def recv(self, size):
        data = self._socket.recv(size)
        return data

    def __del__(self):
        self._socket.close()


# In[3]:


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


# In[13]:


def parse(msg):
    root = ET.fromstring(msg)
    pos_attrib = root.find('Pos').attrib
    pos_act_mes = np.array([
        pos_attrib['X'],
        pos_attrib['Y'],
        pos_attrib['Z'],
        pos_attrib['A'],
        pos_attrib['B'],
        pos_attrib['C']]).astype(np.float64)
    return pos_act_mes


# In[113]:


def robot_command_xml(type_=0,
                      a1=0.0, a2=0.0, a3=0.0, a4=0.0, a5=0.0, a6=0.0,
                      x=0.0, y=0.0, z=0.0, a=0.0, b=0.0, c=0.0,
                      vel=0.0):
    xml = b'<RobotCommand><Type>{type_}</Type><Axis A1="{a1}" A2="{a2}" A3="{a3}" A4="{a4}" A5="{a5}" A6="{a6}"></Axis><Cart X="{x}" Y="{y}" Z="{z}" A="{a}" B="{b}" C="{c}"></Cart><Velocity>{vel}</Velocity></RobotCommand>'
    cmd = xml.format(type_=type_,
                     a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6,
                     x=x, y=y, z=z, a=a, b=b, c=c, vel=vel)
    return cmd


# In[130]:


xml = robot_command_xml(type_=1, a1=10.0, a2=-90.0, a3=90.0, a4=0.0, a5=0.0, a6=0.0, vel=0.1)
print(repr(xml))


# In[ ]:


class CMDTYPE:
    PTP_AXIS = 1
    PTP_CART = 2
    LIN_CART = 3
    PTP_AXIS_REL = 4
    LIN_CART_REL = 5


# In[137]:


c = UDPClient(('192.168.250.20', 54600))
c.send(b'0')


# In[157]:


xml = robot_command_xml(type_=CMDTYPE.PTP_AXIS, a1=-90.0, a2=-90.0, a3=90.0, a4=0.0, a5=90.0, a6=0.0, vel=1.0)
c.send(xml)
xml = robot_command_xml(type_=CMDTYPE.PTP_AXIS, a1=-90.0, a2=-100.0, a3=90.0, a4=0.0, a5=0.0, a6=0.0, vel=1.0)
c.send(xml)
xml = robot_command_xml(type_=CMDTYPE.PTP_AXIS, a1=-80.0, a2=-90.0, a3=90.0, a4=0.0, a5=90.0, a6=0.0, vel=1.0)
c.send(xml)


# In[159]:


xml = robot_command_xml(type_=CMDTYPE.PTP_AXIS_REL, a1=10.0, a2=0.0, a3=0.0, a4=0.0, a5=0.0, a6=0.0, vel=1.0)
c.send(xml)


# In[156]:


xml = robot_command_xml(type_=CMDTYPE.LIN_CART_REL, 
                        x=0.0, 
                        y=0.0, 
                        z=0.1, 
                        a=0.0, 
                        b=0.0, 
                        c=0.0, 
                        vel=1.0)
print(xml)
c.send(xml)


# In[153]:


xml = robot_command_xml(type_=, a1=0.0, a2=-90.0, a3=90.0, a4=0.0, a5=0.0, a6=0.0, vel=1.0)
print(xml)
c.send(xml)
# xml = robot_command_xml(type_=1, a1=0.0, a2=-90.0, a3=90.0, a4=0.0, a5=0.0, a6=0.0, vel=0.1)
# print(xml)
# c.send(xml)


# In[136]:


xml = robot_command_xml(type_=1, a1=-90.0, a2=-90.0, a3=90.0, a4=0.0, a5=0.0, a6=0.0, vel=1.0)
print(xml)
c.send(xml)
xml = robot_command_xml(type_=1, a1=-80.0, a2=-90.0, a3=90.0, a4=0.0, a5=0.0, a6=0.0, vel=1.0)
print(xml)
c.send(xml)


# In[92]:


xml = robot_command_xml(type_=1, a1=0.0, a2=-90.0, a3=90.0, a4=0.0, a5=0.0, a6=0.0, vel=0.1)
print(xml)
c.send(bytes(xml))


# In[ ]:


while True:
    data = c.recv(1024)
    print(data)


# In[11]:


msg = '<RobotState><Pos X="447.171417" Y="1.160460" Z="645.844360" A="-179.999557" B="0.000010" C="-179.999710"></Pos></RobotState>'


# In[1]:


root = ET.


# In[20]:



widgets.FloatText(value=x)


# In[28]:


q = [1,2,3,4,5,6]


# In[41]:


import time


# In[159]:


out = widgets.Output()
display(out)


# In[76]:


with out:
    print('ajajaj')


# In[77]:


out.clear_output()


# In[148]:


@out.capture(clear_output=True)
def printer(msg):
    print(msg)


# In[108]:


function_with_captured_output()


# In[48]:


get_ipython().run_line_magic('pinfo', 'widgets.Output')


# In[169]:


c = UDPClient(("192.168.250.20", 54602))
c.send(b'0')
while True:
    data = c.recv(1024)
    pos = parse(data)
    print(pos)
    


# In[150]:


client = TCPClient("192.168.250.20", 54601)
data = client.recv(1024)
print(data)
print(repr(data))


# In[133]:


# jpos = b'9\r\n'
jpos = b'1 0 -90 90.0 0 90 0 1\r\n'
client.send(jpos)
data = client.recv(1024)
print(data)
data = client.recv(1024)
print(data)


# In[143]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[39]:


q = np.array([10.625208, -96.192123, 116.955833, -5.212444, 1.056723, 177.964569])


# In[52]:


len(jpos)


# In[32]:


import numpy as np


# In[ ]:


data = client.recv(1024)
print(data)


# In[ ]:


type(jpos)


# In[ ]:


def lin_rel(x,y,z,r,p,y_):
    pass


# In[ ]:


client.sendall(b"kkkk")


# In[ ]:


client.recv(1024)


# In[ ]:


controller = KRC4("192.168.250.20", 54601)
robot = AbstractRobot(controller)
robot.activate()


# In[ ]:


INITIAL_POSE = math3d.Transform(math3d.Orientation.new_euler(
    np.deg2rad([-85.84, 0, -180]), "ZYX"), [0.65877, 0.0, 0.5])
# må alltid være en definition av config og joints i ptp første gang.
robot.motion_ptp_move(
    pose=INITIAL_POSE, speed=10, acc=50.0, config=2, joints=3, continuos=False)
print(robot.system_get_robot_pos())


# In[ ]:


# robot.system_get_robot_pos()


# In[ ]:


# # KRC4 KR16 robot
# if True:
#     # Dette er bare en eksempel pose. Alle poses er gitt som math3d object og posisjon er i meter.
#     INITIAL_POSE = math3d.Transform(math3d.Orientation.new_euler(
#         np.deg2rad([-85.84, 0, -180]), "ZYX"), [0.65877, 1.05108, 0.90649])
#     # må alltid være en definition av config og joints i ptp første gang.
#     abs_robot.motion_ptp_move(
#         pose=INITIAL_POSE, speed=10, acc=50.0, config=2, joints=3, continuos=False)
#     print(abs_robot.system_get_robot_pos())

