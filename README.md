# kuka_eki
Control KUKA robots using the Ethernet.KRL interface.

## Usage

1. Select the file `ros_eki.src` in the folder `KRC:\R1\Program\ros` on the teach pendant
2. Start the program and the submit interpreter (the *S* in the upper bar)
3. Start the driver: 
```bash
roslaunch roslaunch kuka_eki_interface kuka_eki_interface.launch robot_ip:=192.168.250.16
```
If you want to visualization, you can use the test file:
```bash
roslaunch roslaunch kuka_eki_interface test_eki.launch robot_ip:=192.168.250.16
```

If everything works as planned, you should now be able to control the robot and visualize the current state in RViz.

### Motion commands

The move the robot in PTP-mode to a point in joint space you can use e.g.
```bash 
rosservice call /kuka_eki_interface/ptp_axis "axis: {a1: 0.0, a2: -90.0, a3: 90.0, a4: 0.0, a5: 45.0, a6: 0.0}
max_velocity_scaling: 0.2" 
```
Note that this command is in *degrees* and not in radians as is customary in ROS. 

Similarly, if you want to move the robot in joint space to a cartesian pose you can use e.g.,
```bash
rosservice call /kuka_eki_interface/ptp_pos "pos: {x: 550.0, y: -200.0, z: 400.0, a: 180.0, b: 45.0, c: -180.0, s: 0, t: 0}
max_velocity_scaling: 0.2" 
```
And, finally, if you want to move linearly to a cartesian pose you can use, e.g., 
```bash
rosservice call /kuka_eki_interface/lin_pos "pos: {x: 550.0, y: -200.0, z: 400.0, a: 180.0, b: 45.0, c: -180.0, s: 0, t: 0}
max_velocity_scaling: 0.2" 
```
Note that the positions are in *millimeters*, and that the Euler angles are in *degrees*. 

## The KUKA Euler angle convention

The Euler angle convention used by KUKA is that you first rotate by the angle *a* about the *z*-axis, then you rotate by the angle *b* about the new *y*-axis, and, finally, you rotate by the angle *c* about the new *x*-axis.

All angles are represented in degrees.

## Possible errors

You might get an error that states that you need to calculate the correct *status* and *turn* values for a PTP motion to a pose. This has to do with setting an umambigues robot configuration for the inverse kinematics solver of the robot controller, e.g. elbow-up or down.

A facility for computing these values will be implemented.