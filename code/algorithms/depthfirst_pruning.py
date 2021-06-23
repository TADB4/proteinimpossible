import copy
from code.classes.protein import Protein
from code.algorithms.constructive_tool import Constructive_alg_tool

"""
Breadfirst looks at all the potential ways of folding a protein, 
by making list containing all the potential fold orders
"""
class Depthfirst_pruning(Constructive_alg_tool):
    def __init__(self, data):
        super().__init__(data)
 
    def potential_fold_order(self):
        """
        Make a list of all fold orders
        """
        depth = len(self.data) 
        stack = [""]

        x = 0

        while len(stack) > 0:
            state = stack.pop()
            state_list = state.split(",")
            state_list.pop()
            fold_options = ["-2", "-1", "1", "2"]
            impossible_orders = ["-2,1,2,-1", "-2,-1,2,1", "2,1,-2,-1","2,-1,-2,1", "1,2,-1,-2", "1,-2,-1,2", "-1,2,1,-2", "-1,-2,1,2", "-2,2", "2,-2", "1,-1", "-1,1"]

            # add a 0 for the fold of the last aminoacid
            if len(state_list) == depth -1:
                state_list.append("0")

            # breadth first algorithm
            if len(state_list) < depth - 1:
                
                # make copy of this state for each option
                for i in fold_options:
                    child = copy.deepcopy(state)
                    child += i

                    # check if oder contains an impossible fold order
                    good_order = True 
                    for order in impossible_orders:
                        if order in str(child):
                            good_order = False

                    # if no impossible fold orders are possible, add to queue     
                    if good_order == True:
                        stack.append(child + ",")

            else:
                # for the complete state lists, only add halve 
                if (x % 2) == 0:
                    self.states.append(state_list)
                
            x = x + 1
