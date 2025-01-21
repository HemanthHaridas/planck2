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

import numpy

def rotation_matrix(axis: list[float], angle: float) -> list[float]:
    """
    Generates a 3D rotation matrix to rotate a vector or point around a specified axis.

    Args:
    -----
        axis (list[float]): A 3D vector (x, y, z) representing the axis of rotation.
                            The axis does not need to be normalized as the function normalizes it.
        angle (float): The angle of rotation in degrees.

    Returns:
    --------
        numpy.ndarray: A 3x3 rotation matrix as a numpy array.
    """
    _axis = numpy.array(axis)
    _norm = _axis / numpy.linalg.norm(_axis)
    _ang  = angle / 2
    
    # Calculate the Euler parameters for the rotation
    _a = numpy.cos(_ang * numpy.pi/180)
    _b, _c, _d = -1*_axis * numpy.sin(_ang * numpy.pi/180)
    
    # Now calculate the rotation matrix
    return numpy.array(
            [
                [_a*_a + _b*_b - _c*_c - _d*_d, 2*(_b*_c - _a*_d), 2*(_a*_c + _b*_d)],
                [2*(_b*_c + _a*_d), _a*_a - _b*_b + _c*_c - _d*_d, 2*(_c*_d - _a*_b)],
                [2*(_b*_d - _a*_c), 2*(_c*_d + _a*_b), _a*_a - _b*_b - _c*_c + _d*_d]
                ]
    )