from code.classes.protein import Protein
import copy

class Tool():
    def __init__(self, data):
        self.data = data
        self.protein = Protein(data) # make protein without folds/locations
        self.protein.terminate = False
        self.change_protein()

    def change_protein(self):
        """
        Change a protein: add folds and restart when protein is invalid
        """
        # try folds until a possible fold is found
        while self.add_folds() == False:
            Protein.clear_protein(self.protein)
            Randomise.__init__(self, self.data)

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
            self.select_fold(aminoacid)  
    
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





        