#  Copyright (c) 2019 Norwegian University of Science and Technology
#  Use of this source code is governed by the BSD 3-Clause license, see LICENSE

import numpy as np
from geometry_msgs.msg import Pose, PoseStamped, Transform


def orientation_to_abc_in_deg(orientation):
    quaternion = np.array([orientation.w,
                           orientation.x,
                           orientation.y,
                           orientation.z])
    abc = np.rad2deg(
        tf.transformations.euler_from_quaternion(quaternion, 'rzyx'))
    return abc


def pose_to_xyzabc_in_mm_deg(pose):
    x, y, z = np.array([pose.position.x,
                        pose.position.y,
                        pose.position.z]) * 1000.0
    a, b, c = orientation_to_abc_in_deg(pose.orientation)
    return [x, y, z, a, b, c]
