import numpy as np
from robots import OmniDirectinalRobot, TwoSteerRobot

if __name__ == "__main__":
    # example of omndidiriction robot calculations
    l = 1
    p = (l, np.pi / 3)  # polar coordinate wheel placement of first wheel
    r = 1  # wheel radii
    robot = OmniDirectinalRobot(r, p)
    print(robot.state)  # get current robot-frame velocties
    robot.wheels[0].w = 1  # set wheel 1 speed
    print(robot.state)  # get new robot-frame velocties
    print(robot.forward)  # get world velocities using forward kinematics
    print(
        robot.inverse([1.15470054, -1.33333333, -2.33333333])
    )  # get wheel velocities from desired real world velocities
