import copy
from queue import Queue
from code.classes.protein import Protein

class Breadthfirst:
    def __init__(self, data):
        self.data = data
        self.states = []
        self.csv_all_scores = []
        self.protein = Protein(data)
        self.potential_fold_order()
        self.try_every_fold()

        
        #self.change_protein()

    # def change_protein(self):
    #     """
    #     Change a protein: add folds and calculate score
    #     """
    #     # try folds until a possible fold is found
    #     while self.add_folds() == False:
    #         Protein.clear_protein(self.protein)
    #         Breadthfirst.__init__(self, self.data)

    def potential_fold_order(self):
        """
        Make a list of all fold orders
        """
        depth = len(self.data) 
        queue = Queue()
        queue.put("")
                
        while not queue.empty():

            state = queue.get()
            state_list = state.split(",")
            state_list.pop()

            # add a 0 for the fold of the last aminoacid
            if len(state_list) == depth -1:
                state_list.append("0")

            # *** create starting molecule

            # breadth first algorithm
            if len(state_list) < depth - 1:
                # make copy of this state for each option
                for i in ["-2", "-1", "1", "2"]:
                    child = copy.deepcopy(state)
                    child += i
                    # *** evt probeer eiwit hier
                    queue.put(child + ",")
            else:
                self.states.append(state_list)
        
        
    def try_every_fold(self):
        """
        Tests all states of folding
        """
        possible_proteins = []
        best_stability = 0
        #csv_all_scores = []
        best_protein = None

        # loop over every state of states
        for state in self.states:

            # make a protein without folds
            protein = Protein(self.data)
            self.protein = protein
            
            # start location
            current_location = [0,0] 

            # loop over aminoacids of protein 
            for i, aminoacid in enumerate(protein.aminoacids):
                fold = state[i]
            
                # calculate future location with this fold
                future_location = self.assign_location(current_location, fold)
                
                # if location is free, fold aminoacid and update information
                if future_location not in protein.occupied:
                    aminoacid.fold = fold
                    aminoacid.location = future_location
                    protein.occupied[i + 1] = copy.deepcopy(future_location)
                    current_location = future_location
                else:
                    break 
            else:
                print("fold invalid")
                continue

            print(protein.score())
            print(protein.occupied)
            protein.stability = protein.stability
            
            # save this (state of the) protein
            possible_proteins.append(protein)

            # save score of this protein to the big csv file
            self.csv_all_scores.append([protein.stability])

            # if this protein has the best score, overwrite previous best protein
            if int(protein.stability) < int(best_stability):
                best_protein = protein
                best_stability = protein.stability
                print("New best value: ", best_stability)
            
        # return the protein with the highest score
        self.protein = best_protein

    
    def assign_location(self, location, fold):   
        """
        Assign the location of a new aminoacid based on the fold
        """  
        new_value = copy.deepcopy(location)
        fold = int(fold)
        
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


    # tips van bas:
    # states niet als self variable maar als return
    # later toepassen: 
        # gelijk testen of deze state kan en al gaan vouwen, zodat je daaropvolgende states kan elimineren (prunen)
        # kijken of dit sneller is dan alles testen