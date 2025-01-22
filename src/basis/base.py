#  Planck
#  Copyright (C) 2024 Hemanth Haridas, University of Utah
#  Contact: hemanthhari23@gmail.com
# 
#  This program is free software: you can redistribute it and/or modify it under
#  the terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or a later version.
# 
#  This program is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#  PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License along with
#  this program.  If not, see <http://www.gnu.org/licenses/>.

from enum import Enum
import numpy
import scipy.special

class Shell_Type(Enum):
    """
    Enumeration for atomic orbital shell types.

    This enum represents the different types of atomic orbital shells commonly used 
    in quantum chemistry calculations. Each shell type is assigned a unique integer value.

    Members:
        S (int): Represents the s-orbital (spherical symmetry), with value 0.
        P (int): Represents the p-orbital (dumbbell shape), with value 1.
        D (int): Represents the d-orbital (cloverleaf shape), with value 2.
        F (int): Represents the f-orbital (complex shapes), with value 3.
        G (int): Represents the g-orbital (higher angular momentum), with value 4.
    """
    S = 0
    P = 1
    D = 2
    F = 3
    G = 4
    
class Shell:
    """
    A class representing a Gaussian basis function used in quantum chemistry calculations.

    Attributes:
    -----------
        shell (list[int]): The angular momentum quantum numbers of the basis function, 
            e.g., [0, 0, 0] for an s-orbital, [1, 0, 0] for a p-orbital in the x-direction.
        exps (list[float]): The Gaussian exponents for the basis function. These determine 
            the width of the Gaussian functions.
        coeffs (list[float]): The contraction coefficients associated with each Gaussian exponent.
            These coefficients define the linear combination of primitive Gaussians forming the basis function.
        center (list[float]): The Cartesian coordinates [x, y, z] of the center of the basis function.

    Methods:
    --------
        __init__(shell: list[int], exps: list[float], coeffs: list[float], center: list[float]):
            Initializes a Basis object with the specified shell, exponents, coefficients, and center.

    Args:
    -----
        shell (list[int]): Angular momentum quantum numbers for the basis function.
        exps (list[float]): List of Gaussian exponents for the basis function.
        coeffs (list[float]): List of contraction coefficients for the basis function.
        center (list[float]): Cartesian coordinates of the center of the basis function.
    """
    def __init__(self, shell: list[int], exps: list[float], coeffs: list[float], center: list[float], is_Normalized: bool) -> None:
        self.shell        = numpy.array(shell)
        self.exponents    = numpy.array(exponents)
        self.coefficients = numpy.array(coefficients)
        self.normcoeffs   = numpy.zeros(self.coefficients.size)
        self.center       = numpy.array(center)
        self.basisindex   = 0
        self.type         = Shell_Type(sum(self.shell))
        
        # Ensure that the shells are normalized
        if not is_Normalized:
            self._normalize()
        
    def _normalize(self) -> None:
        """
        Normalize the basis function.

        This method computes the normalization constant for the Gaussian basis function 
        based on its angular momentum quantum numbers (`shell`). The normalization ensures 
        that the integral of the basis function over all space equals 1.

        Attributes Used:
            shell (list[int]): The angular momentum quantum numbers [l, m, n] of the basis function,
                where l, m, n represent the powers of x, y, z in the Gaussian function.
        """
        _l, _m, _n = self.shell
        _total_moment = sum(self.shell)
        _prefact_pgto = pow(2, 2*_total_moment) * pow(2, 1.5)/scipy.special.factorial2(2*_l-1)/scipy.special.factorial2(2*_m-1)/scipy.special.factorial2(2*_n-1)/pow(numpy.pi, 1.5)
        
        self.normcoeffs = numpy.sqrt(pow(exponent, _total_moment) * pow(self.exponents, 1.5) * prefactorpGTO)
        _prefact_cgto   = pow(numpy.pi, 1.5) * factorial2(2*_l - 1) * factorial2(2*_m - 1) * factorial2(2*_n - 1) / pow(2.0, _total_moment)
        