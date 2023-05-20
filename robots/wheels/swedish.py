from .wheel import Wheel
from numpy import array, sin, cos


class SwedishWheel(Wheel):
    """gamma representing the angle between the main wheel
    plane and the axis of rotation of the small circumferential rollers"""

    type_ = "swedish wheel"

    def __init__(self, r, pos, **kwargs):
        gamma = kwargs.get("gamma", 0)
        self.gamma = gamma
        super().__init__(r, pos, **kwargs)

    @property
    def J(self):
        """rolling constraint"""
        l, a = self.pos
        J = array(
            [
                sin(a + self.b + self.gamma),
                -cos(a + self.b + self.gamma),
                -l * cos(self.b + self.gamma),
            ]
        )
        return J

    @Wheel.w.setter
    def w(self, ang_vel):
        """v = w*r
        get linear velocity from angular"""
        self._w = ang_vel
        self._v = ang_vel * self.r * cos(self.gamma)

    @Wheel.v.setter
    def v(self, lin_vel):
        self._w = lin_vel / self.r * cos(self.gamma)
        self._v = lin_vel
