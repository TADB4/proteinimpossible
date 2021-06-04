
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
        self.score()

    def create_protein(self):
        # keeps creating molecules until the protein is finished
        self.nucleotide = None
        self.molecule_number = None
        location = [0, 0]
        fold = 0
        occupied = []

        # loop over nucleotides of the data and add info to molecule object
        for i, char in enumerate(self.data):

            molecule_number = i
            nucleotide = char
            occupied.append(location)

            # make molecule object and add to molecules list
            molecule = Molecule(nucleotide, molecule_number, location, fold, self.size_data, occupied)
            self.molecules.append(molecule)

            # make dictionary of molecule locations
            self.molecule_locations[str(location)] = molecule
    
            # update location for next molecule
            location = copy.deepcopy(self.molecules[molecule_number].next_location)

            # set fold of the molecule
            fold = copy.deepcopy(self.molecules[molecule_number].next_fold)
        

    def score(self):
        # # loop over molecules in protein
        # for location in self.molecule_locations:
        #     # note score if there is a possible binding
        #     molecule = self.molecule_locations[location]
        #     if molecule.nucleotide == "H":
        #         for i in range(surrounded_by(molecule, H)):
        #             self.stability -= 1
        # print(self.stability)
        pass

    # def surrounded_by(molecule, nucleotide):
    #     surrounded_by = 0
    #     fold_directions = [-1, 1]
    #     #checks for unbound neigbours on bound sides
    #     for folds in fold_directions:
    #         location_neigbour = molecule.location[0] + folds

    #         if self.molecule_locations[location_neigbour] in self.molecule_locations:
    #             nucleotide_neighbour = self.molecule_locations[location_neigbour].molecule.nucleotide

    #             if nucleotide_neighbour == nucleotide:
    #                 surrounded_by += 1
    #     surrounded_by = surrounded_by/2
    #     return surrounded_by
        pass
            # for every richting (rechts, links, boven, onder)
                # check if location +/- 1 is not in dict
                # check if location +/- 2 is in dict
                # als allebei de checks, add location +/- 2 to bindingenlist

            # return bindingen list
        
