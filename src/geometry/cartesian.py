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

from planck.src.geometry.base import BaseMolecule

class Molecule(BaseMolecule):
    """
    A class representing a molecule, inheriting from the BaseMolecule class. This class processes molecular
    structures provided as a string, extracting details such as molecular charge, multiplicity, number of 
    atoms, atomic symbols, and coordinates.

    Attributes:
    -----------
    charge (int) : The molecular charge.
    multi (int)  : The multiplicity of the molecule.
    natoms (int) : The number of atoms in the molecule.
    atoms (list) : A list to store the atomic symbols of the molecule.
    coords (list): A list to store the atomic coordinates as lists of floats.

    Methods:
    --------
    geometry(structure: str) -> None:
        Parses the molecular structure string to populate the molecular attributes such as charge, multiplicity, 
        number of atoms, atomic symbols, and coordinates.
    """

    def geometry(self, structure: str) -> None:
        """
        Parses a molecular structure string to extract molecular properties and atomic data.

        Args:
        -----
        structure (str): A multiline string representing the molecular structure. The structure should follow 
                         a specific format:
                         - The first line contains the molecular charge and multiplicity (space-separated).
                         - Subsequent lines represent atomic data in the format: 
                           "<atomic_symbol> <x_coordinate> <y_coordinate> <z_coordinate>".

        Returns:
        --------
        None: This method does not return a value. It updates the instance attributes (charge, multi, natoms, 
              atoms, and coords).

        Example Input Format:
        ---------------------
        0 1
        H 0.000 0.757 0.586
        O 0.000 0.000 0.000
        H 0.000 -0.757 0.586

        Raises:
        -------
        ValueError: If the input structure string is malformed or missing required data.
        """
        # Split the input structure into lines, ignoring empty ones
        _structure = [line for line in structure.splitlines() if line.strip()]
        
        # Extract charge and multiplicity from the first line
        self.charge = int(_structure[0].split()[0])
        self.multi  = int(_structure[0].split()[1])
        
        # Calculate the number of atoms
        self.natoms = len(_structure) - 1  # Subtract 1 to exclude the first line
        
        # Initialize lists to store atomic symbols and coordinates
        self.atoms  = []
        self.coords = []
        
        # Process each atom line to extract atomic symbols and coordinates
        for _line in _structure[1:]: 
            _atom   = _line.split()[0]  # Extract the atomic symbol
            _coords = [float(_coord) for _coord in _line.split()[1:]]  # Extract and convert coordinates
            self.atoms.append(_atom)  # Append atomic symbol to atoms list
            self.coords.append(_coords)  # Append coordinates to coords list

    def build(self, atoms: list[str], coords: list[list[float]], charge: int, multi: int) -> None:
        """
        Populates the attributes of a molecular object with atomic and molecular data.

        This method is used to initialize or update the molecule's atomic structure,
        spatial coordinates, charge, and multiplicity.

        Args:
        -----
        atoms (list[str])         : A list of atomic symbols representing the types of atoms in the molecule.
        coords (list[list[float]]): A list of lists where each sublist contains the 3D coordinates [x, y, z]
                                    of an atom. The number of sublists should match the number of atoms.
        charge (int): The overall charge of the molecule.
        multi (int) : The spin multiplicity of the molecule (2S + 1), where S is the total spin.

        Returns:
        --------
        None: This method does not return a value. It updates the instance attributes `atoms`, `coords`,
            `charge`, and `multi`.

        Example Usage:
        --------------
        mol = Molecule()
        mol.build(
            atoms  = ["H", "O", "H"],
            coords = [
                        [0.0, 0.757, 0.586], 
                        [0.0, 0.0, 0.0], 
                        [0.0, -0.757, 0.586]
                    ],
            charge = 0,
            multi  = 1
        )
        """
        self.atoms  = atoms
        self.coords = coords
        self.charge = charge
        self.multi  = multi