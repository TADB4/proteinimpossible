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

            print("depth: ", depth)
            print("state, state_list en self.states: ", len(state), len(state_list), len(self.states))

            # add only state options that have the length of the whole protein
            if len(state_list) == depth-1:
                print("in if *********")
                self.states.append(state_list)
                print("self.states if:", self.states)
                                                            #create starting molecule
            if len(state) < depth:
                print("len self.states: ", len(state))
                # make copy of this state for each option
                for i in ["-2", "-1", "1", "2"]:
                    child = copy.deepcopy(state)
                    child += i
                    queue.put(child + ",")
        
        print("self.states:", self.states)

    def try_every_fold(self):
        """
        Tests all states of folding
        """
        # loop over every state of states
        for state in states:
            # make a protein without folds
            protein = Protein(data)
            
            # loop over aminoacids of protein 
            for i, aminoacid in enumerate(protein.aminoacids):
                # calculate future location with this fold
                # assign_location(current_location, fold)

                # if future_location not in occupied:
                    # fold this aminoacid with the corresponding fold 
                    # aminoacid.fold = state[i] 
                    # use assign_location?
                    # update (current) location, occupied etc.

                # else:
                    # go to next state

            # save this (state of the) protein
            # calculate score of this protein 
        
        pass


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