
from .molecule import Molecule
import copy

class Protein:
    def __init__(self, data):
        self.molecules = []
        self.data = data
        self.size_data= len(data)
        self.molecule_locations = {"Location":[], "Molecule":[]}
        self.stability = 0
        
        self.create_protein()
       
    def create_protein(self):
        # keeps creating molecules until the protein is finished
        self.nucleotide = None
        self.molecule_number = None
        location = [0, 0]
        fold = 0
        occupied = []

        for i, char in enumerate(self.data):

            molecule_number = i
            nucleotide = char
            occupied.append(location)
            print(f"protein{occupied}")
            molecule = Molecule(nucleotide, molecule_number, location, fold, self.size_data, occupied)
            self.molecules.append(molecule)
            self.molecule_locations[str(location)] = molecule
    
            location = copy.deepcopy(self.molecules[molecule_number].next_location)

            # set fold of the molecule
            fold = copy.deepcopy(self.molecules[molecule_number].next_fold)
        

    def score():
        # maak een tijdelijke kopie van moleculen dict
        temp_locations = copy.deepcopy(self.molecule_locations)
        # loop over moleculen in eiwit
        for molecule in temp_locations:
            # note score if there is a possible binding
            if molecule.nucleotide == "H" 
                for i in range(surrounded_by(H))
                    self.stability -= 1
            
            # remove molecule from temporary dict to prevent double scores
            self.temp_locations.pop(molecule)
        pass

    def surrounded_by(molecule):
        surrounded_by = 0
        fold_directions = [-1, 1]
        for i in fold_directions:
            if 
         # for every richting (rechts, links, boven, onder)
            # check if location +/- 1 is not in dict
            # check if location +/- 2 is in dict
            # als allebei de checks, add location +/- 2 to bindingenlist

        # return bindingen list
        pass
            

    
    
