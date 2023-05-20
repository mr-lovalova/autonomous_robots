from abc import ABC, abstractmethod
from .wheels import StandardWheel
from .platform import Platform
import numpy as np
from numpy import cos, sin, pi, sqrt


class TwoSteerRobot(Platform):
    """

    Attributes
    ----------

    Methods
    -------
    """

    def __init__(self, w_radii, first_wheel_pos):
        """
        Parameters
        ----------
        front_wheel_pos : tuple
            first wheel should not have a negative alpha
            a wheel is fixed to the platforms by a polar coordinate" (l,alpha)
        d : float or int
            distance to fixed wheel
        """
        wheels = []
        l, first_alpha = first_wheel_pos
        for i in range(2):
            alpha = first_alpha - pi * i
            wheel = StandardWheel(w_radii, (l, alpha), pi * i)
            wheels.append(wheel)
        super().__init__(*wheels)

    @property
    def kinematics(self):
        """should be a 3x3 matrix"""
        J = []
        for count, wheel in enumerate(self.wheels):
            if not count:
                # adding slding constraint for last wheel ( same for both wheels)
                J.append(wheel.C)
            J.append(wheel.J)
        J = np.array(J)
        return J

    def steer(self):
        pass


if __name__ == "__main__":
    l = 1.0
    r = 1
    robot = TwoSteerRobot(r, (l, pi / 3))
    # print(np.around(robot.kinematics, 3))
    print(robot.state)

    # print(robot.forward)
