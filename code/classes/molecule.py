import random

class Molecule:
    def __init__(self, nucleotide, molecule_number, location, fold, size_data):
        self.nucleotide = nucleotide
        self.molecule_number = molecule_number
        self.previous_fold = fold
        self.previous_location = location
        self.size_data = size_data




        self.location = self.assign_location()
        self.fold = self.create_fold()
        self.x_location = None
        self.y_location = None
        

        
    def create_fold(self):
        types = [-2, -1 , 1, 2]

        # assign a random fold and 0 for the last molecule
        if self.molecule_number == self.size_data-1 :
            return 0
        else:
            return random.choice(types)

    def molecule_location(self):
        if self.fold == 1:
            self.x_location +=1
        elif self.fold == -1:
            self.x_location -=1
        elif self.fold == 2:
            self.y_location +=1
        elif self.fold == -2:
            self.y_location -=1

        self.location = [self.x_location, self.y_location] 
        
    def assign_location(self):    
        # assign location 0,0 for the first molecule
        if self.molecule_number == 0:
            return [0,0] 

        new_value = self.previous_location

        # change location value based on fold
        if self.previous_fold == 1:
            new_value[0] += 1
        elif self.previous_fold == -1:
            new_value[0] -= 1
        elif self.previous_fold == 2:
            new_value[1] += 1
        elif self.previous_fold == -2:
            new_value[1] -= 1
        
        return new_value


    # def surrounding(self):
    
    # def is_valid(self):