import random, copy
from code.classes.protein import Protein

class Greedy():
    def __init__(self, data):
        self.data = data
        self.protein = Protein(data) # make protein without folds/locations
        self.protein.terminate = False
        self.change_protein()
        
    def change_protein(self):
        """
        Change a protein: add folds and calculate score
        """
        # try folds until a possible fold is found
        while self.add_folds() == False:
            Protein.clear_protein(self.protein)
            Greedy.__init__(self, self.data) 

    def add_folds(self):
        """
        Adds folds to an existing aminoacid sequence
        """
        for aminoacid in self.protein.aminoacids:
            # folds the next aminoacid
            self.create_fold(aminoacid)
            
            # restarts function when protein blocked itself of
            if self.protein.terminate == True:
                print("Protein folded in itself, collision on:", aminoacid.location, "creating new protein.")
                return False

        return True

    def create_fold(self, aminoacid):
        """
        Picks a fold for the next aminoacid
        COPIED FROM RANDOMISE
        """
        # assign a fold of 0 for the last aminoacid
        if aminoacid.aminoacid_number == len(self.data) - 1:
            return
        # assign a random fold for the rest of the aminoacids
        else:
            #return folds
            self.select_best_fold(aminoacid)

    def select_best_fold(self, aminoacid):
        """
        Select the best fold for this aminoacid
        """
        # set ways of folding 
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
            
            self.check_potential_fold(fold, possible_loc, aminoacid, neighbours_folds)

        # terminate if no neighbours are possible
        if len(neighbours_folds) == 0:
            self.protein.terminate = True

        # choose fold with highest amount of neighbours
        best_fold = max(neighbours_folds, key=neighbours_folds.get)
        
        # update location information of this aminoacid
        self.protein.occupied[aminoacid.aminoacid_number + 1] = self.assign_location(location, best_fold)
        self.protein.aminoacids[aminoacid.aminoacid_number + 1].location = self.assign_location(location, best_fold)
        self.protein.aminoacids[aminoacid.aminoacid_number + 1].fold = best_fold
        return

    def check_potential_fold(self, fold, possible_loc, aminoacid, neighbours_folds):
        """
        Check if this 
        """
            
        nucleotides = ['H', 'P', 'C']
        total_neighbours = 0
            
        # count for each nucleotide how many neighbours it has
        for nucleotide in nucleotides:
            neighbours = Protein.surrounded_by(self.protein, possible_loc, nucleotide, aminoacid.aminoacid_number)
            total_neighbours = total_neighbours + neighbours

            neighbours_folds[fold] = total_neighbours 
            
    def assign_location(self, location, fold):   
        """
        Assign the location of a new aminoacid based on the fold
        """  
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
                                       
