from code.algorithms import randomise, greedy
import copy

class Molecule:
    def __init__(self, nucleotide, molecule_number, location, fold, size_data, occupied, molecule_locations):
        self.nucleotide = nucleotide
        self.molecule_number = molecule_number
        self.fold = fold
        self.location = location
        self.size_data = size_data
        self.occupied = occupied
        self.molecule_locations = molecule_locations
        self.next_fold = 0 
        self.next_location = [0,0] 
        self.terminate = False

        # picks where to fold the next molecule to
        self.create_fold()

    def tryout_new_location(self, types):
        '''
        Test if a new location is possible
        '''
        try_location = [0, 0]
        
        # try locations until a not-occupied location is found and not all folds are checked
        while try_location in self.occupied: #and types:
            # tells protein it has no valid way to fold
            if len(types) == 0:
                print("protein folded in itself")
                self.terminate = True
                return

            # choose random fold
            # current_type = greedy.Greedy(types, occupied)
            current_type = randomise.Random_pick(types)
            
            # remove current fold from types to prevent using the same fold
            types.remove(current_type)

            self.next_fold = current_type
            
            # check if location is possible 
            try_location = self.assign_location(current_type)

            self.next_fold = current_type

            # if location is not possible, try next fold
            if try_location in self.occupied:
                continue
            # if location is possible, use location
            else:
                self.next_location = try_location
                return 

        
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
            return
        # assign a random fold for the rest of the molecules
        else:
            self.tryout_new_location(types)
            
            
    def assign_location(self, fold):   
        '''
        Assign the location of a new molecule based on the fold
        '''  
        new_value = copy.deepcopy(self.location)
        
        # change location value based on fold
        if fold == 1:
            new_value[0] += 1
        elif fold == -1:
            new_value[0] -= 1
        elif fold == 2:
            new_value[1] += 1
        elif fold == -2:
            new_value[1] -= 1
        
        return new_value


    def surrounded_by(location, molecule_number, nucleotide):
        '''
        Determine which molecules are directly surrounding the current molecule
        '''
        surrounded_by = 0
        fold_directions = [0, 1]

        # checks for unbound neighbours on bound sides
        for folds in fold_directions:
            location_neighbour = copy.deepcopy(location)
            location_neighbour[folds] = copy.deepcopy(location[folds]) + 1
            location_neighbour = tuple(location_neighbour)
            
            # checks wether molecule is bound to neighbour
            if self.neighbour_is_not_bound(molecule_number, location_neighbour) == True:

                # if there is a neighbour at that location, assign to variable
                if tuple(location_neighbour) in self.molecule_locations:
                    nucleotide_neighbour = self.molecule_locations[location_neighbour].nucleotide
                    if nucleotide_neighbour == nucleotide:
                        surrounded_by += 1
        return surrounded_by


    def neighbour_is_not_bound(self, molecule_number, location_neighbour):
        '''
        Checks if neighbour is not bound to the molecule
        '''
        # unless it's the starting molecule checks if it's the molecule bound from
        if molecule_number != 0 and tuple(self.occupied[molecule_number - 1]) == location_neighbour:
            return False
        # unless it's the last molecule checks if it's the molecule binding to
        elif molecule_number != self.size_data - 1 and tuple(self.occupied[molecule_number + 1]) == location_neighbour: 
            return False
        else:
            return True