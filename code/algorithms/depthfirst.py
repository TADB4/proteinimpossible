import copy
from code.classes.protein import Protein
from code.algorithms.constructive_tool import Constructive_alg_tool

"""
Implements the breadfirst algorithm that  looks at all the potential ways of folding a protein, 
by making list containing all the potential fold orders
"""
class Depthfirst(Constructive_alg_tool):
    def __init__(self, data):
        super().__init__(data)

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
                