
from .molecule import Molecule
import copy

class Protein:
    def __init__(self, data):
        self.molecules = []
        self.data = data
        self.size_data= len(data)
        # self.x_value = 0
        # self.y_value = 0
        # self.location= [0, 0]
        
        self.create_protein()
       
    def create_protein(self):
        # keeps creating molecules until the protein is finished
        self.nucleotide = None
        self.molecule_number = None
        location = [0, 0]
        fold = 0
        
        for i, char in enumerate(self.data):

            molecule_number = i
            nucleotide = char
            self.molecules.append(Molecule(nucleotide, molecule_number, location, fold, self.size_data))
            location = copy.deepcopy(self.molecules[molecule_number].location)
            fold = copy.deepcopy(self.molecules[molecule_number].fold)
    
    # def update_location(self, molecule_number):
    #     # make new location based on fold
    #     molecule = self.molecules[molecule_number]
    #     self.x_value = molecule.location[0] + 1
    #     self.y_value = molecule.location[1] + 1
        
        
    # def is_valid(selfu):
    #     #checks wether new molecule is not on another molecule

    # def reconfigure(self):
    #     #solves self blocking error

    # def stability(self):
    #     #calculates stability value of the created protein

    
    
