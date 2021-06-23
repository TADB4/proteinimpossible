"""
Holds all the variables for an Aminoacid building block of the Protein class
"""
class Aminoacid:
    def __init__(self, aminoacid_type, aminoacid_number, location, fold): 
        self.aminoacid_type = aminoacid_type
        self.aminoacid_number = aminoacid_number
        self.fold = fold
        self.location = location
       