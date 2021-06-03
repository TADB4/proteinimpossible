
from .molecule import Molecule

class Protein:
    def __init__(self, data):
        self.molecules = []
        self.data = data
        self.create_protein()
        
    def create_protein(self):
        # keeps creating molecules until the protein is finished
        self.nucleotide = None
        self.molecule_number = None
        for i, char in enumerate(self.data):
            molecule_number = i
            nucleotide = char
            self.molecules.append(Molecule(nucleotide, molecule_number))
        return self.molecules
            
    # def is_valid(self):
    #     #checks wether new molecule is not on another molecule

    # def reconfigure(self):
    #     #solves self blocking error

    # def stability(self):
    #     #calculates stability value of the created protein

    
    
