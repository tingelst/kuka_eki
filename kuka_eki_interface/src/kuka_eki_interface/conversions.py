# Copyright (c) 2019 Norwegian University of Science and Technology
# Use of this source code is governed by the BSD 3-Clause license, see LICENSE
#
# Author: Lars Tingelstad

import numpy as np

import tf
from geometry_msgs.msg import Pose


def abc_in_deg_to_quaternion(abc):
    a, b, c = np.deg2rad(abc)
    quaternion = tf.transformations.quaternion_from_euler(a, b, c, 'rzyx')
    return quaternion


def quaternion_to_abc_in_deg(quaternion):
    abc = np.rad2deg(
        tf.transformations.euler_from_quaternion(quaternion, 'rzyx'))
    return abc


def pose_to_xyzabc_in_mm_deg(pose):
    x, y, z = np.array(
        [pose.position.x, pose.position.y, pose.position.z]) * 1000.0
    quaternion = np.array(
        [pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w])
    a, b, c = quaternion_to_abc_in_deg(quaternion)
    return np.array([x, y, z, a, b, c])


def xyzabc_in_mm_deg_to_pose(xyzabc):
    x, y, z, a, b, c = xyzabc
    pose = Pose()
    pose.position.x = x / 1000.0
    pose.position.y = y / 1000.0
    pose.position.z = z / 1000.0
    quaternion = abc_in_deg_to_quaternion(np.array([a, b, c]))
    pose.orientation.x = quaternion[0]
    pose.orientation.y = quaternion[1]
    pose.orientation.z = quaternion[2]
    pose.orientation.w = quaternion[3]
    return pose
