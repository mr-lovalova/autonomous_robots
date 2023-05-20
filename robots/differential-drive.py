from sympy import (
    simplify,
    sin,
    cos,
    atan2,
    sqrt,
    pi,
    Matrix,
    zeros,
    Symbol,
    BlockMatrix,
    shape,
)
from abc import ABC, abstractmethod
import transformations
from ..wheels import SwedishWheel, StandardWheel, FixedStandardWheel
from platform import Platform


class DifferentialDriveRobot(Platform):
    def _get_constraints(self, *wheels):
        J = []
        Cn = []
        iterated = []
        for wheel in wheels:
            J.append([wheel.constraints[0]])
            if wheel in iterated:
                continue
            Cn.append([wheel.constraints[1]])
            iterated.append(wheel)
        self._J = Matrix(BlockMatrix(J))
        self._Cn = Matrix(BlockMatrix(Cn))
        self._C = Matrix.vstack(self._J, self._Cn)
