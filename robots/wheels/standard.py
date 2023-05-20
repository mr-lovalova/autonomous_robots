from abc import ABC, abstractmethod

from .wheel import Wheel


class StandardWheel(Wheel):
    def _make_constraints(self, pos):
        l, a = pos
        crolling = Matrix(
            [sin(a + self.beta), -cos(a + self.beta), -l * cos(self.beta)]
        ).T
        cslide = Matrix([cos(a + self.beta), sin(a + self.beta), l * sin(self.beta)]).T
        return crolling, cslide


class FixedStandardWheel(StandardWheel):
    def __init__(self, r, pos, b, vel=0):
        super().__init__(r, pos, vel)
        self.calc_constraints(b)
