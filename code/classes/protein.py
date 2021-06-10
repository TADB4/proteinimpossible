from .molecule import Molecule
import copy

class Protein:
    def __init__(self, data):
        self.molecules = []
        self.data = data
        self.size_data = len(data)
        self.molecule_locations = {}
        self.stability = 0
        self.occupied = []
        self.create_protein()
        self.score()

    def create_protein(self):
        '''
        Keeps creating molecules until the protein is finished
        '''
        while self.try_protein() == False:
            self.clear_protein()
        
        print(len(self.occupied))
    
        
    def try_protein(self):
        '''
        Tries to create a protein one time and returns false if protein 
        folds on itself
        '''
        location = [0, 0]
        fold = 0

        # loop over nucleotides of the data and add info to molecule object
        for i, char in enumerate(self.data):
            molecule_number = i
            nucleotide = char
            self.occupied.append(location)

            # make molecule object and add to molecules list
            molecule = Molecule(nucleotide, molecule_number, location, fold, self.size_data, self.occupied, self.molecule_locations)

            # restarts function when protein blocked itself of
            if molecule.terminate == True:
                print("Restart:", molecule.location)
                return False
            else:
                self.molecules.append(molecule)

                # add molecule to dictionary of molecule locations
                self.molecule_locations[tuple(location)] = molecule
        
                # update location for next molecule
                location = copy.deepcopy(self.molecules[molecule_number].next_location)

                # update fold for next molecule
                fold = copy.deepcopy(self.molecules[molecule_number].next_fold)
        return True
        
    
    def clear_protein(self): 
        '''
        Clear the current protein
        '''
        list.clear(self.occupied)
        dict.clear(self.molecule_locations)
        list.clear(self.molecules)     


    def score(self):
        '''
        Calculate score of a protein
        '''
        # loop over molecules in protein
        for loc in self.molecule_locations:
            # select molecule 
            molecule = self.molecule_locations[loc]
            
            # calculate how often H is surrounded by H or C
            print(molecule.location)
            print(molecule.molecule_number)
            if molecule.nucleotide == "H":
                self.stability = self.stability + (-1 * Molecule.surrounded_by(molecule.location, molecule.molecule_number, "H" )) + (-1 * Molecule.surrounded_by(molecule.location, molecule.molecule_number, "C" ))
            elif molecule.nucleotide == "C":
                self.stability = self.stability + (-5 * Molecule.surrounded_by(molecule.location, "C", molecule.molecule_number)) + (-1 * Molecule.surrounded_by(molecule.location, "H", molecule.molecule_number))

                
        
    
        
