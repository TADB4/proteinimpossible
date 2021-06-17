import copy
from queue import Queue
from code.classes.protein import Protein

class Breadthfirst:
    def __init__(self, data):
        self.data = data
        self.states = []
        self.protein = Protein(data) # make protein without folds/locations
        self.protein.terminate = False
        self.potential_fold_order()
        #self.change_protein()

    def change_protein(self):
        """
        Change a protein: add folds and calculate score
        """
        # try folds until a possible fold is found
        while self.add_folds() == False:
            Protein.clear_protein(self.protein)
            Breadthfirst.__init__(self, self.data)

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
                
                      
        print("self.states:", len(self.states))

    # def try_every_fold(self):
    #     """
    #     Tests all states of folding
    #     """
    #     possible_proteins = []

    #     # loop over every state of states
    #     for state in states:
    #         # make a protein without folds
    #         protein = Protein(data)

    #         # start location
    #         current_location = [0,0]
            
    #         # loop over aminoacids of protein 
    #         for i, aminoacid in enumerate(protein.aminoacids):
    #             fold = state[i]

    #             # calculate future location with this fold
    #             future_location = self.assign_location(current_location, fold)

    #             # if location is free, fold aminoacid and update information
    #             if future_location not in protein.occupied:
    #                 aminoacid.fold = fold
    #                 aminoacid.location = future_location
    #                 protein.occupied.append(future_location)
    #                 current_location = future_location
    #             else:
    #                 break 

    #         # save this (state of the) protein
    #         possible_proteins
    #         # calculate score of this protein 
        
    #     pass


    # def assign_location(self, location, fold):   
    #     """
    #     Assign the location of a new aminoacid based on the fold
    #     """  
    #     new_value = copy.deepcopy(location)
        
    #     # change location value based on fold
    #     if fold == 1:
    #         new_value[0] += 1
    #     elif fold == -1:
    #         new_value[0] -= 1
    #     elif fold == 2:
    #         new_value[1] += 1
    #     elif fold == -2:
    #         new_value[1] -= 1
        
    #     return new_value        


    # tips van bas:
    # states niet als self variable maar als return
    # later toepassen: 
        # gelijk testen of deze state kan en al gaan vouwen, zodat je daaropvolgende states kan elimineren (prunen)
        # kijken of dit sneller is dan alles testen