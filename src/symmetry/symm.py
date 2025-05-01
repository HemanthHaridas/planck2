from planck.src.geometry.cartesian import Molecule as Cartesian
from planck.src.geometry.zmatrix import Molecule as ZMatrix
import typing
import pymsym

def symmetrize_molecule(molecule: typing.Union[Cartesian, ZMatrix]) -> None:
    _atomic_numbers = molecule.atomicnumbers
    _atomic_coordinates = molecule.coords
    
    
    
