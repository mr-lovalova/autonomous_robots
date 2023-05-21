import numpy as np
from numpy import cos, sin, arccos, arcsin, arctan, tan, pi, rad2deg, deg2rad, sqrt
from robots import ExamRobot2018, ExamRobot2021, OmniDirectinalRobot, TwoSteerRobot


#### examples
def exam2018():
    speed = 0.5
    angle = arctan(1 / 0.5)
    xdot, ydot = cos(angle) * speed, sin(angle) * speed
    robot = ExamRobot2018()
    result = robot.inverse(xdot, ydot, 0)
    return result


def exam2019():
    robot = ExamRobot2018()  # same kinematics as 2018
    robot.wheels[0].w = 0
    robot.wheels[1].w = -2
    robot.wheels[2].w = 2
    result = robot.forward
    return result


def exam2021():
    speed = 0.3
    r = 1
    w = 0.3 / r
    desired = (0, speed, w)
    robot = ExamRobot2021()
    result = robot.inverse(*desired)
    return result


def exam2021_other():
    ### just try all forward values
    robot = ExamRobot2021()
    robot.wheels[0].w = -6.9
    robot.wheels[1].w = 2.1
    robot.wheels[2].w = 2.1
    result = robot.forward
    return result


def omni():
    l = 1
    r = 1
    robot = OmniDirectinalRobot(r, (l, pi / 3))
    print(robot.state)
    robot.wheels[0].w = 1
    print(robot.state)
    # print(np.around(robot.kinematics, 3))
    # robot.state = [1.15470054, -1.33333333, -2.33333333]
    print(robot.inverse([1.15470054, -1.33333333, -2.33333333]))


def twosteer2021():
    l = 0.3
    robot = TwoSteerRobot(r, (l / 2, pi / 2))
    robot.wheels[0].w = 1
    robot.wheels[1].w = 0
    print(robot.state)


if __name__ == "__main__":
    # print(exam2018())
    # print(exam2019())
    print(exam2021_other())
    # robot = twosteer()
    # robot = omni()
    # angle = arctan(0.1 / 0.15)
    # print(rad2deg(angle))
    # print(180 - rad2deg(angle))
    # r = sqrt(0.15**2 + 0.1**2)
    # print(r)
