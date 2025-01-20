from planck.src.geometry.base import BaseMolecule

class Molecule(BaseMolecule):
    def geometry(self, structure: str) -> None:
        return NotImplemented
    def build(self) -> None:
        return NotImplemented