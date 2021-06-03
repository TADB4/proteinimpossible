import random


class Molecule:
    def __init__(self, nucleotide, molecule_number, location):
        self.nucleotide = nucleotide
        self.molecule_number = molecule_number
        self.fold = self.create_fold()
        self.x_location = None
        self.y_location = None
        self.location = self.assign_location()
        self.previous_location = location

    def create_fold(self):
        types = [-2, -1 , 1, 2]
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
        
    def assign_location():    
        # assign location 0,0 for the first molecule
        if self.molecule_number == 0:
            return [0,0] 

        new_value = self.previous_location[0] + 1
        return new_value

    # def next_molecule(self):
    #     self.molecule_number 

    # def surrounding(self):
    
    # def is_valid(self):