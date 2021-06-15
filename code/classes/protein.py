from .molecule import Molecule
import copy

class Protein:
    def __init__(self, data):
        self.data = data # input string of nucleotide sequence
        self.molecules = []
        self.occupied = [] # locations in order of assignment
        self.stability = 0
        self.terminate = False
        self.create_protein()
        
    def create_protein(self):
        '''
        Keeps creating molecules until a correct protein is finished
        '''
        while self.try_protein() == False:
            self.clear_protein()

    def try_protein(self):
        '''
        Tries to create a protein one time and returns false if protein 
        folds on itself
        '''
        location = [0, 0]
        fold = 0
        
        # loop over nucleotides of the data and add info to molecule object
        for i, char in enumerate(self.data):
            molecule_number = i
            nucleotide = char   
            
            # make molecule object and add to molecules list
            molecule = Molecule(nucleotide, molecule_number, location, fold)
            self.occupied.append(molecule.location)
            self.molecules.append(molecule)

            # make a line orientation as default
            location = [0, len(self.data) + i]
        return 
              
    def create_fold(self, molecule):
        '''
        Picks a fold for the next molecule
        '''
        if molecule.molecule_number == molecule.size_data - 1:
            return
        else:
            self.tryout_new_location()

    def tryout_new_location(self):
        '''
        Tests if a new location is possible
        '''
        try_location = [0, 0]
        
        # try locations until a not-occupied location is found and not all folds are checked
        while try_location in self.occupied:

            # folds north everytime
            current_type = 2
            
            # check if location is possible 
            try_location = self.assign_location(current_type)

            # if location is not possible, try next fold
            if try_location in self.occupied:
                continue
            # if location is possible, use location
            else:
                self.next_location = try_location
                return        
    
    def clear_protein(self): 
        '''
        Clear information of this protein
        '''
        list.clear(self.occupied)

    def score(self):
        '''
        Calculate score of a protein
        '''
        # loop over molecules in protein
        for molecule in self.molecules:
            # calculate how often H is surrounded by H or C
            if molecule.nucleotide == "H":
                self.stability = self.stability + (-1 * self.surrounded_by(molecule.location, "H", molecule.molecule_number)) + (-1 * self.surrounded_by(molecule.location, "C", molecule.molecule_number))
            # calculate how often H is surrounded by C
            elif molecule.nucleotide == "C":
                self.stability = self.stability + (-5 * self.surrounded_by(molecule.location, "C", molecule.molecule_number)) + (-1 * self.surrounded_by(molecule.location, "H", molecule.molecule_number))
        self.stability = self.stability/2
        
    def surrounded_by(self, molecule_location, nucleotide, molecule_number):
        '''
        Determine which molecules are directly surrounding the current molecule
        '''
        surrounded_by = 0
        fold_directions = [0, 1]
        neg_pos = [1, -1]

        # checks for unbound neighbours for x and y
        for folds in fold_directions:
            location_neighbour = copy.deepcopy(molecule_location)

            # checks negative and positive directions
            for value in neg_pos:
                # save neighbour location
                location_neighbour[folds] = copy.deepcopy(molecule_location[folds]) + value
                
                # checks wether molecule is bound to neighbour
                if self.neighbour_is_not_bound(molecule_number, location_neighbour) == True:
                    # if there is a neighbour at that location, assign to variable
                    if location_neighbour in self.occupied:
                        nucleotide_neighbour = self.molecules[self.occupied.index(location_neighbour)].nucleotide
                        if nucleotide_neighbour == nucleotide:
                            surrounded_by += 1             
        return surrounded_by

    def neighbour_is_not_bound(self, molecule_number, location_neighbour):
        '''
        Checks if neighbour is not bound to the molecule
        '''
        # unless it's the starting molecule checks if it's the molecule bound from
        if molecule_number != 0 and self.occupied[molecule_number - 1] == location_neighbour:
            return False
            self.molecules[molecule_number].molecule_number - 1
        # unless it's the last molecule checks if it's the molecule binding to
        elif molecule_number != len(self.data) - 1 and self.occupied[molecule_number + 1] == location_neighbour: 
            return False
        else:
            return True
                
        
    
    