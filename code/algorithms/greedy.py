import copy
import random
from code.classes.protein import Protein

class Greedy:
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
            Greedy.__init__(self, self.data) 

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
        COPIED FROM RANDOMISE
        '''
        # assign a fold of 0 for the last molecule
        if molecule.molecule_number == len(self.data) - 1:
            return
        # assign a random fold for the rest of the molecules
        else:
            #return folds
            self.select_best_fold(molecule)

    # OLD FUNCTION:
    def select_best_fold(self, molecule):
        # set ways of folding 
        fold_options = [2, 1, -1, -2]
        folds = random.sample(fold_options, len(fold_options))

        neighbours_folds = {}

        # current location 
        location = molecule.location
        count = 0
        
        # check potential folds 
        for fold in folds:
            count = count + 1

            # select new location based on this fold
            possible_loc = self.assign_location(location, fold)
            
            # check if not occupied
            if possible_loc in self.protein.occupied:
                continue
            
            nucleotides = ['H', 'P', 'C']
            total_neighbours = 0
            
            # count for each nucleotide how many it are a neighbour
            for nucleotide in nucleotides:
                neighbours = Protein.surrounded_by(self.protein, possible_loc, nucleotide, molecule.molecule_number)
                total_neighbours = total_neighbours + neighbours

            
            neighbours_folds[fold] = total_neighbours

        # terminate if no neighbours are possible
        if len(neighbours_folds) == 0:
            self.protein.terminate = True

        
        # choose fold with highest amount of neighbours
        best_fold = max(neighbours_folds, key=neighbours_folds.get)
        
        # update location information of this molecule
        self.protein.occupied[molecule.molecule_number + 1] = self.assign_location(location, best_fold)
        self.protein.molecules[molecule.molecule_number + 1].location = self.assign_location(location, best_fold)
        self.protein.molecules[molecule.molecule_number + 1].fold = best_fold
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
                                       
