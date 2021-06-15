import random, copy
from code.classes.protein import Protein

class Randomise():
    def __init__(self, data):
        self.data = data
        self.protein = Protein(data) # make protein without folds/locations
        self.protein.terminate = False
        self.change_protein()

    def change_protein(self):
        '''
        Change a protein: add folds and calculate score
        '''
        # try folds until a possible fold is found
        while self.add_folds() == False:
            Protein.clear_protein(self.protein)
            Randomise.__init__(self, self.data)

    def add_folds(self):
        '''
        Adds folds to an existing molecule sequence
        '''
        for molecule in self.protein.molecules:
            # folds the next molecule
            self.create_fold(molecule)
            
            # restarts function when protein blocked itself of
            if self.protein.terminate == True:
                print("Protein folded in itself, collision on:", molecule.location, "creating new protein.")
                return False

        return True

    def create_fold(self, molecule):
        '''
        Picks a fold for the next molecule
        '''
        # assign a fold of 0 for the last molecule
        if molecule.molecule_number == len(self.data) - 1:
            return
        # assign a random fold for the rest of the molecules
        else:
            #return folds
            self.tryout_new_location(molecule)

    def tryout_new_location(self, molecule):
        '''
        Test if a new location is possible
        '''
        # set ways of folding 
        folds = [-2, -1 , 1, 2]
            
        # keeps it from immediately folding back on itself
        if molecule.fold != 0:
            folds.remove(molecule.fold * -1)

        try_location = [0, 0]
            
        # try locations until a not-occupied location is found 
        while try_location in self.protein.occupied: #and folds:
            
            # tells protein it has no valid way to fold
            if len(folds) == 0:
                self.protein.terminate = True
                return

            # choose random fold
            current_fold = random.choice(folds)
                
            # remove current fold from folds to prevent using the same fold
            folds.remove(current_fold)
                
            # check if location is possible 
            try_location = self.assign_location(molecule.location, current_fold)

            # if location is not possible, try next fold
            if try_location in self.protein.occupied:
                continue
            # if location is possible, use location to make a new molecule
            else:
                self.protein.occupied[molecule.molecule_number + 1] = try_location
                self.protein.molecules[molecule.molecule_number + 1].location = try_location
                self.protein.molecules[molecule.molecule_number + 1].fold = current_fold 
                return           
            
    def assign_location(self, location, fold):   
        '''
        Assign the location of a new molecule based on the fold
        '''  
        new_value = copy.deepcopy(location)
        
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
                                       