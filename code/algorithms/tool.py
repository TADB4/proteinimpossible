from code.classes.protein import Protein

class Tool:
    def __init__:
        pass
    
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
            self.select_best_fold(aminoacid) #of self.tryout_new_location(aminoacid)  
        