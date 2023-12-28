from abc import ABC, abstractmethod
from .wheels import SwedishWheel
from .platform import Platform
from numpy import array, cos, sin, pi, sqrt, arctan
import numpy as np


class ExamRobot(Platform):
    @property
    def kinematics(self):
        return self.k

    @property
    def forward(self):
        """Calculate world velocity from kinematics"""
        w = np.array([[wheel.w] for wheel in self.wheels])
        v_world = np.linalg.inv(self.R) @ np.linalg.inv(self.kinematics) @ w
        return v_world

    def inverse(self, xdot, ydot, thetadot):
        """Calculate wheel velocties from world velocties"""
        v = np.array([[xdot], [ydot], [thetadot]])
        v_world = np.linalg.solve(np.linalg.inv(self.kinematics), v)
        return v_world


class ExamRobot2018(ExamRobot):
    def __init__(self):
        """Used in the sets 2018 and 2019
        used for exam assignment only .... so sjit code"""
        self.k = array([[0, -2, -0.3], [-sqrt(3), 1, -0.3], [sqrt(3), 1, -0.3]])
        l = 1  # arbitrary value placeholder
        r = self.k[0][-1] / l  ## placeholder
        wheel1 = SwedishWheel(r, (l, 0))
        wheel2 = SwedishWheel(r, (l, -(2 * pi / 3)))
        wheel3 = SwedishWheel(r, (l, (2 * pi / 3)))
        super().__init__(wheel1, wheel2, wheel3)


class ExamRobot2021(ExamRobot):
    def __init__(self):
        """Used in the sets 2018 and 2019
        used for exam assignment only .... so sjit code"""
        self.k = array([[0, -20, -3], [-sqrt(30), 10, -3], [sqrt(30), 10, -3]])
        l = 1  # arbitrary value placeholder
        r = self.k[0][-1] / l  ## placeholder
        wheel1 = SwedishWheel(r, (l, 0))
        wheel2 = SwedishWheel(r, (l, -(2 * pi / 3)))
        wheel3 = SwedishWheel(r, (l, (2 * pi / 3)))
        super().__init__(wheel1, wheel2, wheel3)


class ExamRobot2022(ExamRobot):
    def __init__(self):
        self.k = array([[0, -20, -3], [-10 * sqrt(3), 10, -3], [10 * sqrt(3), 10, -3]])
        l = 1  # arbitrary value placeholder
        r = self.k[0][-1] / l  ## placeholder
        wheel1 = SwedishWheel(r, (l, 0))
        wheel2 = SwedishWheel(r, (l, -(2 * pi / 3)))
        wheel3 = SwedishWheel(r, (l, (2 * pi / 3)))
        super().__init__(wheel1, wheel2, wheel3)
