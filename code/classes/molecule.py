import random

class Molecule:
    def __init__(self, nucleotide, molecule_number, location, fold, size_data, occupied):
        self.nucleotide = nucleotide
        self.molecule_number = molecule_number
        self.fold = fold
        self.location = location
        self.size_data = size_data
        self.occupied = occupied
        self.terminate = False

        self.next_fold = 0 #self.create_fold()
        self.next_location =  [0,0] #self.assign_location()
        
        self.create_fold()
        
        
    def create_fold(self):
        # set fold types
        types = [-2, -1 , 1, 2]
        
        #keeps it from immediately folding back on itself
        if self.fold != 0:
            types.remove(self.fold*-1)

        # assign a fold of 0 for the last molecule
        if self.molecule_number == self.size_data - 1:
            return 0
        # assign a random fold for the rest of the molecules
        else:
            try_location = [0,0]
            # try locations until a not-occupied location is found and not all folds are checked
            while try_location in self.occupied and types:
                # choose random fold
                current_type = random.choice(types)
                self.next_fold = current_type

                # remove current fold from types
                types.remove(current_type)

                print("type:", current_type)
                
                # check if location is possible 
                try_location = self.assign_location()
                print("try_location:", try_location)
                print("occupied:", self.occupied, "if")
                if try_location in self.occupied:
                    print("Continue")
                    continue
                elif try_location not in self.occupied:
                    print("Done?")
                else:
                    print("Done")
                    self.next_location = try_location
                    return True

                # if all types are checked without result
                # if not types:
                    # terminate = True

            # self.next_fold = random.choice(types)
            # try_location = self.assign_location()
            # if try_location in self.occupied:
            #     self.create_fold()
            # else:
            #     self.next_location = try_location
        
    def assign_location(self):    
        #assign location 0,0 for the first molecule
        # if self.molecule_number == 0:
        #     return [0,0] 
        print(f"occupied: {self.occupied} location 1")
        new_value = self.location

        print(f"occupied: {self.occupied} location 2")
        # change location value based on fold
        if self.next_fold == 1:
            new_value[0] += 1
        elif self.next_fold == -1:
            new_value[0] -= 1
        elif self.next_fold == 2:
            new_value[1] += 1
        elif self.next_fold == -2:
            new_value[1] -= 1
        print(f"occupied: {self.occupied} location 3")
        return new_value


    
    