from abc import ABC, abstractmethod
import numpy as np
from numpy import cos, sin


class Platform(ABC):
    """need kinematics need to return an invertible matrix"""

    _R = np.array(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
    )

    def __init__(self, *wheels):
        """R is given as rotation from platform to world"""
        self.wheels = wheels
        self.radii = np.diag([wheel.r for wheel in self.wheels])

    @property
    @abstractmethod
    def kinematics(self):
        """robot kinematics described as J @"""
        pass

    @property
    def R(self):
        return self._R

    @R.setter
    def R(self, theta):
        self._R = np.array(
            [
                [cos(theta), sin(theta), 0],
                [-sin(theta), cos(theta), 0],
                [0, 0, 1],
            ]
        )

    @property
    def state(self):
        """xdot, ydot, thetadot, in robot frame"""
        w = np.array([[wheel.w] for wheel in self.wheels])
        _state = np.linalg.inv(self.kinematics) @ self.radii @ w
        return _state

    @state.setter
    def state(self, new):
        """takes tuple of desired state (xdot,ydot,thetadot) in robot frame"""
        # new = np.array([[val] for val in new])
        w = np.linalg.inv(self.radii) @ self.kinematics @ new
        for count, wheel in enumerate(self.wheels):
            wheel.w = w[count][0]

    @property
    def forward(self):
        """Calculate world velocity from wheel velocies
        thus p is the vector  = [omega1, omega2, ... for all wheels]
        """
        v_world = np.linalg.inv(self.R) @ self.state
        return v_world

    def inverse(self, v):
        """Calculate wheel velocties from linear world velocties"""
        v = np.array([[val] for val in v])
        v_robot = np.linalg.inv(self.radii) @ self.kinematics @ self.R @ v
        self.state = self.R @ v
        print("STATE", self.state)
        print("V", v_robot)
        return v_robot
