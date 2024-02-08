### planck2
<p align="justify"> planck2 is a rewrite of the older [plank.py](https://github.com/HemanthHaridas/plank.py) project, aiming to take advantage of the modular design and efficient use of python libraries with minimal external bindings written in C++ and (or) Fortran. This code is not aimed at being as optimized or efficient as the commerically avaialble quantum chemistry codes like Gaussian, Orca or NWChem, but is meant to provide a toy model for the regular users to teach quantum chemistry and (or) build their own codes based on this library.</p>

#### Usage Instructions
<p align="justify"> The code allows for the generation of a molecule object either from a z-matrix representation or a cartesian representation. You can either specify the required representation in the python code, or you can read it from an input file. </p> 

##### Input file in z-matrix representation for water molecule.

``` python
# Assuming that you have a z-matrix file of the name water.zmat

from planck2.core.geometry.builder import Molecule
water_molecule  =   Molecule()
water_molecule.create_molecule_zmatrix_from_file(input_file = "water.zmat")
```

##### Input file in z-matrix representation for water molecule.

``` python
water_geometry="""
H
O   1   1.10
H   2   1.10    1   109.45
"""

from planck2.core.geometry.builder import Molecule
water_molecule  =   Molecule()
water_molecule.create_molecule_zmatrix_from_input(zmat = water_molecule, charge = 0, multiplicity = 1)
```