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

from planck.src.calculators.base import BaseCalculator
from planck.src.exceptions.base import ChargeMultiplicityError
from planck.src.geometry.cartesian import Molecule as Cartesian
from planck.src.geometry.zmatrix import Molecule as ZMatrix
import numpy
import typing
 
class RHF(BaseCalculator):
    """
    Restricted Hartree-Fock (RHF) Calculator Class.

    This class implements the Restricted Hartree-Fock (RHF) method for performing
    quantum chemistry calculations on molecular systems. It inherits from the
    `BaseCalculator` abstract base class and provides an implementation for the
    required `calculator` method.

    The RHF method assumes that all electrons in a closed-shell molecule are paired
    and occupy the same spatial orbitals. This class supports molecular representations
    in both Cartesian and Z-Matrix coordinate systems.

    Parameters
    ----------
    molecule : typing.Union[Cartesian, ZMatrix]
        A molecular geometry object, either in Cartesian coordinates or 
        Z-Matrix format, describing the structure of the molecule.

    Methods
    -------
    calculator():
        Implements the RHF computational workflow. This method must be called to
        perform the RHF calculation on the provided molecular geometry.
    
    Attributes
    ----------
    molecule : typing.Union[Cartesian, ZMatrix]
        The molecular geometry object passed during initialization.
    """
    
    def calculator(self, molecule: typing.Union[Cartesian, ZMatrix], basis_sets: typing.Dict[str, str]):
        """
        Initializes the RHF calculator with the molecular geometry.

        Parameters
        ----------
        molecule : typing.Union[Cartesian, ZMatrix]
            A molecular geometry object, either in Cartesian or Z-Matrix format.
        """
        self.molecule = molecule
        _sanity_check = self.check_multiplicity()
        
    def check_multiplicity(self) -> typing.Union[bool]:
        _total_electrons = numpy.sum(self.molecule.atomicnumbers) + self.molecule.charge

        # Check if the total number of electrons in even and multiplicity is one => No unpaired electrons
        if (self.molecule.multi < 1):
            raise ChargeMultiplicityError(message = f"It is impossible to have a multiplicity of {self.molecule.multi}")
        if (_total_electrons % 2 == 0) and (self.molecule.multi == 1):
            return True
        else:
            raise ChargeMultiplicityError(message = f"The combination of {self.molecule.charge} and {self.molecule.multi} is not allowed. Please check the input carefully!")
        return False
        
            