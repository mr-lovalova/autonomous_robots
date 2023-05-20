from abc import ABC, abstractmethod

from .wheel import Wheel
import numpy as np
from numpy import sin, cos, pi


class FixedStandardWheel(Wheel):
    type_ = "Fixed StandardWheel"

    def __init__(self, r, pos, b, **kwargs):
        super().__init__(r, pos, b=b, **kwargs)

    @property
    def J(self):
        l, a = self.pos
        J = np.array([sin(a + self.b), -cos(a + self.b), -l * cos(self.b)])
        return J

    @property
    def C(self):
        l, a = self.pos
        C = np.array([cos(a + self.b), sin(a + self.b), l * sin(self.b)])
        return C


class StandardWheel(FixedStandardWheel):
    type_ = "Standard Wheel"

    def __init__(self, r, pos, b, **kwargs):
        range_ = kwargs.get("range", pi / 3)
        self.range = range_
        super().__init__(r, pos, b=b, **kwargs)

    @Wheel.b.setter
    def b(self, value):
        # TODO assert value is within range
        self._b = value
