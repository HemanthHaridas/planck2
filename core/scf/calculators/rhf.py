"""
    Planck2 is a Python code to perform Hartree-Fock calculations on molecules.
    Copyright (C) 2024  Hemanth Haridas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from    core.geometry.builder import Molecule
import  sys

class RHF:
    def __init__(self, molecule: Molecule, basis_set: str = "sto-3g", scf_cycles: int = 100, conv_tol: float = 1.0e-12) -> None:
        self.basis      = None
        self.diis       = True
        self.basis_set  = basis_set  
        self.scf_cycles = scf_cycles
        self.conv_tol   = conv_tol
        self.molecule   = molecule
        self.n_alpha    = 0
        self.n_beta     = 0
    
    def check_charge_multiplicity(self) -> bool:
        _total_electrons    = sum(self.molecule.atomNumbers) + self.molecule.charge
        try:
            assert _total_electrons % 2 == 0, f"[ERROR] Total number of electrons {_total_electrons} is not even. Given charge {self.molecule.charge} is not valid for the multiplicity {self.molecule.multiplicity}. Exiting!"
        except AssertionError as _error_message:
            print(_error_message)
            return False
        self.n_alpha    =   _total_electrons // 2
        self.n_beta     =   _total_electrons // 2
        return True
    
    def build_integrals(self) -> None:
        if self.check_charge_multiplicity():
            pass
