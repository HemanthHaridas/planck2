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

from core.geometry.builder import Molecule

class RHF:
    def __init__(self, molecule: Molecule) -> None:
        self.basis      = None
        self.molecule   = molecule
    
    def check_charge_multiplicity(self) -> None:
        pass
    
    def build_integrals(self) -> None:
        pass
    