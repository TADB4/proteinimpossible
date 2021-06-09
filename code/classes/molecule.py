
from code.algorithms import randomise
import copy

class Molecule:
    def __init__(self, nucleotide, molecule_number, location, fold, size_data, occupied):
        self.nucleotide = nucleotide
        self.molecule_number = molecule_number
        self.fold = fold
        self.location = location
        self.size_data = size_data
        self.occupied = occupied
        self.next_fold = 0 
        self.next_location =  [0,0] 

        # picks where to fold the next molecule to
        self.create_fold()

    def tryout_new_location(self, types):
        '''
        Test if a new location is possible
        '''
        try_location = [0,0]
        
        # try locations until a not-occupied location is found and not all folds are checked
        while try_location in self.occupied and types:
            # choose random fold
            current_type = randomise.Random_pick(types)
            self.next_fold = current_type

            # remove current fold from types to prevent using the same fold
            types.remove(current_type)
            if not types:
                return print("protein folded in itself")

            # check if location is possible 
            try_location = self.assign_location()

            # if location is not possible, try next fold
            if try_location in self.occupied:
                continue
            # if location is possible, use location
            else:
                self.next_location = try_location
                return True

        
    def create_fold(self):
        '''
        Picks a fold for the next molecule
        '''
        # set fold types
        types = [-2, -1 , 1, 2]
        
        # keeps it from immediately folding back on itself
        if self.fold != 0:
            types.remove(self.fold * -1)

        # assign a fold of 0 for the last molecule
        if self.molecule_number == self.size_data - 1:
            return 0
        # assign a random fold for the rest of the molecules
        else:
            self.tryout_new_location(types)
            
            
    def assign_location(self):   
        '''
        Assign the location of a new molecule based on the fold
        '''  
        new_value = copy.deepcopy(self.location)
        
        # change location value based on fold
        if self.next_fold == 1:
            new_value[0] += 1
        elif self.next_fold == -1:
            new_value[0] -= 1
        elif self.next_fold == 2:
            new_value[1] += 1
        elif self.next_fold == -2:
            new_value[1] -= 1
            
        return new_value


    
    