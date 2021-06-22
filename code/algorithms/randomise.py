import random, copy
from code.classes.protein import Protein
from .tool import Tool

class Randomise(Tool):
    def __init__(self, data):
        super().__init__(data)

    def select_fold(self, aminoacid):
        """
        Test if a new fold is possible
        """
        # set ways of folding 
        folds = [-2, -1 , 1, 2]
            
        # keeps it from immediately folding back on itself
        if aminoacid.fold != 0:
            folds.remove(aminoacid.fold * -1)

        try_location = [0, 0]
            
        # try locations until a not-occupied location is found 
        while try_location in self.protein.occupied:
            
            # tells protein it has no valid way to fold
            if len(folds) == 0:
                self.protein.terminate = True
                return

            # choose random fold
            current_fold = random.choice(folds)
                
            # remove current fold from folds to prevent using the same fold
            folds.remove(current_fold)
                
            # check if location is possible 
            try_location = self.assign_location(aminoacid.location, current_fold)

             # if location is possible, use location to make a new aminoacid
            if try_location not in self.protein.occupied:
                self.protein.occupied[aminoacid.aminoacid_number + 1] = try_location
                self.protein.aminoacids[aminoacid.aminoacid_number + 1].location = try_location
                self.protein.aminoacids[aminoacid.aminoacid_number + 1].fold = current_fold 
                return  
                                   

                                       