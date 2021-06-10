from .molecule import Molecule
import copy

class Protein:
    def __init__(self, data):
        self.molecules = []
        self.data = data
        self.size_data = len(data)
        self.molecule_locations = {}
        self.stability = 0
        self.occupied = []
        self.create_protein()
        self.score()

    def create_protein(self):
        '''
        Keeps creating molecules until the protein is finished
        '''
        self.nucleotide = None
        self.molecule_number = None
        location = [0, 0]
        fold = 0

        occupied = self.occupied

        # loop over nucleotides of the data and add info to molecule object
        for i, char in enumerate(self.data):

            molecule_number = i
            nucleotide = char
            occupied.append(location)

            # make molecule object and add to molecules list
            molecule = Molecule(nucleotide, molecule_number, location, fold, self.size_data, occupied)

            # restarts function when protein blocked itself of
            if molecule.terminate == True:
                print("Restart")

                location = [0, 0]
                fold = 0
                self.occupied = []
                self.create_protein()

            self.molecules.append(molecule)

            # add molecule to dictionary of molecule locations
            self.molecule_locations[tuple(location)] = molecule
    
            # update location for next molecule
            location = copy.deepcopy(self.molecules[molecule_number].next_location)

            # update fold for next molecule
            fold = copy.deepcopy(self.molecules[molecule_number].next_fold)
        

    def score(self):
        '''
        Calculate score of a protein
        '''
        # loop over molecules in protein
        for loc in self.molecule_locations:
            # select molecule 
            molecule = self.molecule_locations[loc]
            
            # calculate how often H is surrounded by H or C
            if molecule.nucleotide == "H":
                self.stability = self.stability + (-1 * self.surrounded_by(molecule, "H")) + (-1 * self.surrounded_by(molecule, "C"))
            # calculate how often H is surrounded by C
            elif molecule.nucleotide == "C":
                self.stability = self.stability + (-5 * self.surrounded_by(molecule, "C")) + (-1 * self.surrounded_by(molecule, "H"))

 
    def surrounded_by(self, molecule, nucleotide):
        '''
        Determine which molecules are directly surrounding the current molecule
        '''
        surrounded_by = 0
        fold_directions = [0, 1]

        # checks for unbound neighbours on bound sides
        for folds in fold_directions:
            location_neighbour = copy.deepcopy(molecule.location)
            location_neighbour[folds] = copy.deepcopy(molecule.location[folds]) + 1
            location_neighbour = tuple(location_neighbour)
            
            # checks wether molecule is bound to neighbour
            if self.neighbour_is_not_bound(molecule, location_neighbour) == True:

                # if there is a neighbour at that location, assign to variable
                if tuple(location_neighbour) in self.molecule_locations:
                    nucleotide_neighbour = self.molecule_locations[location_neighbour].nucleotide
                    if nucleotide_neighbour == nucleotide:
                        surrounded_by += 1
        return surrounded_by


    def neighbour_is_not_bound(self, molecule, location_neighbour):
        '''
        Checks if neighbour is not bound to the molecule
        '''
        # unless it's the starting molecule checks if it's the molecule bound from
        if molecule.molecule_number != 0 and tuple(self.occupied[molecule.molecule_number - 1]) == location_neighbour:
            return False
        # unless it's the last molecule checks if it's the molecule binding to
        elif molecule.molecule_number != self.size_data - 1 and tuple(self.occupied[molecule.molecule_number + 1]) == location_neighbour: 
            return False
        else:
            return True
                
        
    
        
