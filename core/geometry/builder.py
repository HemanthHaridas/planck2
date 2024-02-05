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

import  numpy    as numpy
import  math     as math
import  sys      as sys
import  os       as os
import  time     as time

class Molecule:
    def __init__(self) -> None:
        self.nAtoms             =   0
        self.atomCoordinates    =   []
        self.atomNames          =   []
        self.atomNumbers        =   []
        self.charge             =   0
        self.multiplicity       =   1

    def create_molecule_zmatrix_from_file(self, input_file: str) -> None:
        with open(input_file) as _inpObject:
            _file_data              =   _inpObject.readlines()
            _charge,_multiplicity   =   _file_data[0].split()
            _internal_coordinates   =   _file_data[2:]
            _natoms                 =   len(_internal_coordinates)

            self.natoms             =   _natoms
            self.atomCoordinates    =   numpy.zeros((_natoms, 3))
            self.atomNumbers        =   numpy.zeros(_natoms)
            self.charge             =   int(_charge)
            self.multiplicity       =   int(_multiplicity)  

            # if only one atom, place it at origin
            self.atomNames.append(_internal_coordinates[0].split()[0])
            self.atomCoordinates[0,:]   =   numpy.zeros(3)

            # for second atom, we need a distance, and place it
            # along the positive x-axis

            self.atomNames.append(_internal_coordinates[1].split()[0])
            self.atomCoordinates[1][0]  =   float(_internal_coordinates[1].split()[2])
        
            # generate a coordinate frame with the connecting atom 
            # at the center and the next atom along the x-axis. This
            # places the third atom along the x-y plane.

            self.atomNames.append(_internal_coordinates[2].split()[0])
            _bond_length    =   float(_internal_coordinates[2].split()[2])
            _bond_angle     =   float(_internal_coordinates[2].split()[4])
            _index_atom     =   int(_internal_coordinates[2].split()[1]) - 1
            _next_atom      =   int(_internal_coordinates[2].split()[3]) - 1
            if _index_atom == 1:
                _bond_angle =   180 - _bond_angle

            # calculate the unit vector with the bond angle
            self.atomCoordinates[2][0]  =   _bond_length * math.cos(_bond_angle * math.pi/180)
            self.atomCoordinates[2][1]  =   _bond_length * math.sin(_bond_angle * math.pi/180)
            self.atomCoordinates[2, :]  =   self.atomCoordinates[2, :] + self.atomCoordinates[_index_atom, :]

            # now place the remaining atoms
            for _atom_index in range(3, _natoms):
                self.atomNames.append(_internal_coordinates[_atom_index].split()[0])
                _bond_length    =   float(_internal_coordinates[_atom_index].split()[2])
                _bond_angle     =   180 - float(_internal_coordinates[_atom_index].split()[4])
                _bond_dihedral  =   180 - float(_internal_coordinates[_atom_index].split()[6])
                _index_atom     =   int(_internal_coordinates[_atom_index].split()[1]) - 1
                _second_atom    =   int(_internal_coordinates[_atom_index].split()[3]) - 1
                _third_atom     =   int(_internal_coordinates[_atom_index].split()[5]) - 1 

                _location_x     =   _bond_length * math.cos(_bond_angle * math.pi/180)
                _location_y     =   _bond_length * math.sin(_bond_angle * math.pi/180) * math.cos(_bond_dihedral * math.pi/180)
                _location_z     =   _bond_length * math.sin(_bond_angle * math.pi/180) * math.sin(_bond_dihedral * math.pi/180)
                
                _vector_ab          =   self.atomCoordinates[_third_atom, :] - self.atomCoordinates[_second_atom, :]
                _vector_bc          =   self.atomCoordinates[_index_atom, :] - self.atomCoordinates[_second_atom, :]
                _vector_ab          =   _vector_ab / numpy.linalg.norm(_vector_ab)
                _vector_bc          =   _vector_bc / numpy.linalg.norm(_vector_bc)
                _normal_abc         =   numpy.cross(_vector_ab, _vector_bc) 
                _normal_abc         =   _normal_abc / numpy.linalg.norm(_normal_abc)
                _normal_bcd         =   numpy.cross(_normal_abc, _vector_bc)
                _transform_matrix   =   numpy.zeros((3, 3))

                _transform_matrix[:, 0] =   _vector_bc
                _transform_matrix[:, 1] =   _normal_bcd
                _transform_matrix[:, 2] =   _normal_abc
                _transformed_point      =   numpy.dot(_transform_matrix, numpy.array([_location_x, _location_y, _location_z]))
                
                self.atomCoordinates[_atom_index, :]    =   _transformed_point + self.atomCoordinates[_index_atom, :]

    def create_molecule_cartesian_from_file(self, input_file: str) -> None:
        with open(input_file) as _inpObject:
            _file_data              =   _inpObject.readlines()
            _charge,_multiplicity   =   _file_data[0].split()
            _cartesian_coordinates  =   _file_data[2:]
            _natoms                 =   len(_cartesian_coordinates)

            self.natoms             =   _natoms
            self.atomCoordinates    =   numpy.zeros((_natoms, 3))
            self.atomNumbers        =   numpy.zeros(_natoms)
            self.charge             =   int(_charge)
            self.multiplicity       =   int(_multiplicity) 

            for _atom_index, _atom in enumerate(_cartesian_coordinates):
                self.atomNames.append(_atom.split()[0])
                self.atomCoordinates[_atom_index,:] =   [float(coord) for coord in _atom.split()[1:]]
    
    def create_molecule_zmatrix_from_input(self, zmat: str) -> None:
        pass

    def create_molecule_cartesian_from_input(self, cartesian: str) -> None:
        pass
    
    def print_cartesian_coordinates(self) -> None:
        for _atomname, _atomcoords in zip(self.atomNames, self.atomCoordinates):
            print("{:<5s}{:10.3f}{:10.3f}{:10.3f}".format(_atomname, _atomcoords[0], _atomcoords[1], _atomcoords[2]))
