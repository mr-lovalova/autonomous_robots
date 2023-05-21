import numpy as np
from numpy import cos, sin, arccos, arcsin, arctan, tan, pi
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
    robot = twosteer()
    # robot = omni()
