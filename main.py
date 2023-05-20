import numpy as np
from numpy import cos, sin, arccos, arcsin, arctan, tan, pi, sqrt
from robots import ExamRobot2018, ExamRobot2021, OmniDirectinalRobot, TwoSteerRobot


if __name__ == "__main__":
    l = 1.0
    r = 1
    robot = TwoSteerRobot(r, (l, pi / 3))
    # print(np.around(robot.kinematics, 3))
    print(robot.state)

    # print(robot.forward)
