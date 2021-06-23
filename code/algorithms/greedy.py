import random, copy
from code.classes.protein import Protein
from .tool import Tool

"""
Greedy look ahead algorithm depth(1) which prioritises the 
amount of neighbours an aminoacid when chosing where to fold to
"""
class Greedy(Tool):
    def __init__(self, data):
        super().__init__(data)

    def select_fold(self, aminoacid):
        """
        Select the best fold for this aminoacid
        """
        # set ways of folding (randomised)
        fold_options = [2, 1, -1, -2]
        folds = random.sample(fold_options, len(fold_options))

        # current location 
        location = aminoacid.location
        neighbours_folds = {}
        
        # check potential folds 
        for fold in folds:
            # select new location based on this fold
            possible_loc = self.assign_location(location, fold)
            
            # check if not occupied
            if possible_loc in self.protein.occupied:
                continue
            
            # check how many neighbours are the result of a fold
            self.check_potential_fold(fold, possible_loc, aminoacid, neighbours_folds)

        # terminate if no neighbours are possible
        if len(neighbours_folds) == 0:
            self.protein.terminate = True

        # choose fold with highest amount of neighbours
        best_fold = max(neighbours_folds, key=neighbours_folds.get)
        
        # update location information of this aminoacid
        self.protein.occupied[aminoacid.aminoacid_number + 1] = Tool.assign_location(self.protein, location, best_fold)
        self.protein.aminoacids[aminoacid.aminoacid_number + 1].location = Tool.assign_location(self.protein, location, best_fold)
        self.protein.aminoacids[aminoacid.aminoacid_number].fold = best_fold
        return

    def check_potential_fold(self, fold, possible_loc, aminoacid, neighbours_folds):
        """
        Count in how many neighbours a fold results
        """
        aminoacid_types = ['H', 'P', 'C']
        total_neighbours = 0
            
        # count for each aminoacid how many neighbours it has
        for aminoacid_type in aminoacid_types:
            neighbours = Protein.surrounded_by(self.protein, possible_loc, aminoacid_type, aminoacid.aminoacid_number)
            total_neighbours = total_neighbours + neighbours
            neighbours_folds[fold] = total_neighbours 
            
                                       
