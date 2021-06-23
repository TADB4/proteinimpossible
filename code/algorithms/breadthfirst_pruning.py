import copy
from queue import Queue
from code.classes.protein import Protein
from code.algorithms.constructive_tool import Constructive_alg_tool

"""
Works the same as the breadthfirst class but prunes impossible fold orders 
and only saves half of the results to reduce memory costs
"""
class Breadthfirst_pruning(Constructive_alg_tool):
    def __init__(self, data):
        super().__init__(data)
        # self.data = data
        # self.states = []
        # self.csv_all_scores = []
        # self.protein = Protein(data)
        # self.potential_fold_order()
        # print("Orders made, Trying all the orders...")
        # self.try_every_fold()  

    def potential_fold_order(self):
        """
        Make a list of all fold orders
        """
        depth = len(self.data) 
        queue = Queue()
        queue.put("")

        x = 0
                
        while not queue.empty():

            state = queue.get()
            state_list = state.split(",")
            state_list.pop()
            fold_options = ["-2", "-1", "1", "2"]
            impossible_orders = ["-2,1,2,-1", "-2,-1,2,1", "2,1,-2,-1","2,-1,-2,1", "1,2,-1,-2", "1,-2,-1,2", "-1,2,1,-2", "-1,-2,1,2", "-2,2", "2,-2", "1,-1", "-1,1"]
            
            # add a 0 for the fold of the last aminoacid
            if len(state_list) == depth -1:
                state_list.append("0")

            # for the state list that is not 'complete', apply breadth first algorithm
            if len(state_list) < depth - 1:
                
                # make copy of this state for each option
                for i in fold_options:
                    child = copy.deepcopy(state)
                    child += i

                    # check if oder contains an impossible fold order
                    good_order = True
                    for order in impossible_orders:
                        if order in str(child) :
                            good_order = False

                    # if no impossible fold orders are possible, add to queue     
                    if good_order == True:
                        queue.put(child + ",")
            else:
                # for the complete state lists, only add halve 
                if (x % 2) == 0:       
                    self.states.append(state_list)
            
            x = x + 1
                
    # def try_every_fold(self):
    #     """
    #     Tests all states of folding
    #     """
    #     # possible_proteins = []
    #     best_stability = 0
    #     best_protein = None

    #     # loop over every state of states
    #     for state in self.states:
    #         # make a protein without folds
    #         self.protein = Protein(self.data)
            
    #         # start location
    #         current_location = [0,0]

    #         # start csv output file
    #         csv_rows = []
    #         csv_rows.append(['amino','fold'])
            
    #         self.apply_fold(current_location, state, csv_rows)

    #         # calculate stability
    #         self.protein.stability = self.protein.score()

    #         # add score to csv rows
    #         csv_rows.append(['score', self.protein.stability])

    #         # save score of this protein to the big csv file
    #         self.csv_all_scores.append([self.protein.stability])

    #         # if this protein has the best score, overwrite previous best protein
    #         if int(self.protein.stability) < int(best_stability):
    #             best_protein = self.protein
    #             best_stability = self.protein.stability
    #             self.protein.csv_best_score = csv_rows
    #             print("New best score:", self.protein.stability)
            
    #     # return the protein with the highest score
    #     self.protein = best_protein
    
    # def apply_fold(self, current_location, state, csv_rows):
    #     """
    #     Applies the fold for every state
    #     """
    #     for i, aminoacid in enumerate(self.protein.aminoacids):
            
    #         # # set location that is calculated with previous fold
    #         aminoacid.location = current_location
    #         self.protein.occupied[i] = copy.deepcopy(current_location)

    #         fold = state[i]

    #         # add fold to csv output file
    #         csv_rows.append([aminoacid.aminoacid_type, fold])
        
    #         # calculate future location with this fold
    #         future_location = Tool.assign_location(self.protein, current_location, fold)
            
    #         # if location is free, fold aminoacid and update information
    #         if future_location not in self.protein.occupied:
    #             aminoacid.fold = fold
    #             current_location = future_location
    #         else:
    #             break    
