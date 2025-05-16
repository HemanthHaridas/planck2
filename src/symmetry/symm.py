import typing
import pymsym

# from pymsym.pymsym import Elements

def detect_symmetry(atom_coords: typing.List[typing.List[float]], atom_numbers: typing.List[int], atom_names: typing.List[str])-> typing.Union[typing.List[typing.List[float]], typing.List[int]]:

    # get the symmetrized coordinates
    _msym_elements = []
    for atom, name, coord in zip(atom_numbers, atom_names, atom_coords):
        _msym_elements.append(pymsym.pymsym.Element(name = name, coordinates = coord))
    
    with pymsym.Context(elements = _msym_elements) as ctx:
        _pg = ctx.find_symmetry() # get the point group
        _pg = ctx.symmetrize_elements()
    
