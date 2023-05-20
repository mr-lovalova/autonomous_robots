from abc import ABC, abstractmethod
from wheels import SwedishWheel
from platform import Platform
from numpy import array, cos, sin, pi, sqrt
import numpy as np


class ExamRobot(Platform):
    def __init__(self):
        """Used in the sets 2018 and 2019
        used for exam assignment only .... so sjit code"""
        self.k = array([[0, -2, -0.3], [-sqrt(3), 1, -0.3], [sqrt(3), 1, -0.3]])
        l = 1  # arbitrary value placeholder
        r = self.k[0][-1] / l  ## placeholder
        wheel1 = SwedishWheel(r, (l, 0), w=0)
        wheel2 = SwedishWheel(r, (l, -(2 * pi / 3)), w=-2)
        wheel3 = SwedishWheel(r, (l, (2 * pi / 3)), w=2)
        super().__init__(wheel1, wheel2, wheel3)

    @property
    def kinematics(self):
        return self.k

    @property
    def forward(self):
        """Calculate world velocity from wheel velocies
        thus p is the vector  = [omega1, omega2, ... for all wheels]
        """
        w = self.wheels_w
        v_world = np.linalg.inv(self.R) @ np.linalg.inv(self.kinematics) @ w
        return v_world

    def inverse(self, xdot, ydot, thetadot):
        """Calculate wheel velocties from linear world velocties"""
        v = np.array([[xdot], [ydot], [thetadot]])
        v_world = np.linalg.solve(np.linalg.inv(self.kinematics), v)
        return v_world


if __name__ == "__main__":
    robot = ExamRobot()
    print(np.around(robot.kinematics, 3))
    print(robot.forward)
    # print(robot.inverse(0.2236, 0.4472, 0))
