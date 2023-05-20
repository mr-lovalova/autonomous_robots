import numpy as np
from numpy import cos, sin, arccos, arcsin, arctan, tan
from robots import ExamRobot2018, ExamRobot2021, OmniDirectinalRobot


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


if __name__ == "__main__":
    print(exam2018())
    print(exam2019())
