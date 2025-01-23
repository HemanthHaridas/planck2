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

from abc import ABC, abstractmethod

class BaseCalculator(ABC):
    """
    Abstract base class (ABC) for implementing calculator classes for quantum chemistry calculations.

    This class defines the structure for creating calculators that can perform 
    Hartree-Fock (HF) and Møller-Plesset second-order perturbation theory (MP2) calculations. 
    Derived classes must implement the `calculator` method to define specific computational workflows.

    Methods
    -------
    calculator():
        Abstract method that must be implemented in subclasses to perform 
        Hartree-Fock or MP2 calculations or their variations.
    """
    @abstractmethod
    def calculator(self) -> None:
        """
        Abstract method to perform quantum chemistry calculations.
        
        This method should be overridden by subclasses to include the specific
        logic for Hartree-Fock or MP2 calculations. The implementation should 
        handle the setup of necessary computational parameters and execute the 
        calculation workflow.
        
        Raises
        ------
        NotImplementedError
            If the method is not implemented in a subclass.
        """
        pass