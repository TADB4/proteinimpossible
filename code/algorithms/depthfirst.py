import copy
from code.classes.protein import Protein
from code.algorithms.constructive_tool import Constructive_alg_tool

"""
Breadfirst looks at all the potential ways of folding a protein, 
by making list containing all the potential fold orders
"""
class Depthfirst(Constructive_alg_tool):
    def __init__(self, data):
        super().__init__(data)
        # self.data = data
        # self.states = []
        # self.csv_all_scores = []
        # self.protein = Protein(data)
        # self.potential_fold_order()
        # Tool.try_every_fold(self.protein)  

    def potential_fold_order(self):
        """
        Make a list of all fold orders
        """
        depth = len(self.data) 
        stack = [""]
                
        while len(stack)>0:

            state = stack.pop()
            state_list = state.split(",")
            state_list.pop()
            fold_options = ["-2", "-1", "1", "2"]
            
            # add a 0 for the fold of the last aminoacid
            if len(state_list) == depth -1:
                state_list.append("0")

            # breadth first algorithm
            if len(state_list) < depth - 1:
                
                # make copy of this state for each option
                for i in fold_options:
                    child = copy.deepcopy(state)
                    child += i
                    stack.append(child + ",")
            else:
                self.states.append(state_list)
                
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
    #             print("Best protein in if: ", best_protein)
    #             best_stability = self.protein.stability
    #             self.protein.csv_best_score = csv_rows
    #             print("New best score:", self.protein.stability)
            
    #     # return the protein with the highest score
    #     self.protein = best_protein
    
    # def apply_fold(self, current_location, state, csv_rows):
    #     """
    #     Applies the fold for all states
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
      
