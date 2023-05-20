from abc import ABC, abstractmethod

from numpy import array


class Wheel(ABC):
    """a wheel is fixed to the platforms by a polar coordinate" (l,alpha)
    r = radius of wheel
    initial_vel = speed of wheel"""

    def __init__(self, r, pos, **kwargs):
        w = kwargs.get("w", 0)
        b = kwargs.get("b", 0)
        self.r = r
        self._b = b
        self.pos = pos
        self.w = w

    @property
    @abstractmethod
    def J(self):
        pass

    @property
    def v(self):
        """v = w*r
        get linear velocity from angular"""
        return self._v

    @v.setter
    def v(self, lin_vel):
        self._w = lin_vel / self.r
        self._v = lin_vel

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, ang_vel):
        self._w = ang_vel
        self._v = ang_vel * self.r

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    def __str__(self):
        return f"A {self.type_} with radius: {self.r}, ang_velocity: {self.w}"
