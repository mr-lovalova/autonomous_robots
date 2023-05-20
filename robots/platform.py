from abc import ABC, abstractmethod
import numpy as np


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
        # TODO add functionalty to change rotation matrix
        pass

    @property
    def wheels_w(self):
        state = [[wheel.w] for wheel in self.wheels]
        return np.array(state)

    @property
    def forward(self):
        """Calculate world velocity from wheel velocies
        thus p is the vector  = [omega1, omega2, ... for all wheels]
        """
        w = self.wheels_w
        v_world = (
            np.linalg.inv(self.R) @ np.linalg.inv(self.kinematics) @ self.radii @ w
        )
        return v_world

    def inverse(self, xdot, ydot, thetadot):
        """Calculate wheel velocties from linear world velocties"""
        v = np.array([[xdot], [ydot], [thetadot]])
        v_world = np.linalg.inv(self.radii) @ self.kinematics @ self.R @ v
        return v_world
