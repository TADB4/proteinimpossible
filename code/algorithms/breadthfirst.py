import copy
from queue import Queue
from code.classes.protein import Protein
from code.algorithms.constructive_tool import Constructive_alg_tool

"""
Breadfirst looks at all the potential ways of folding a protein, 
by making list containing all the potential fold orders
"""
class Breadthfirst(Constructive_alg_tool):
    def __init__(self, data):
        super().__init__(data)  

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
                    queue.put(child + ",")
            else:
                self.states.append(state_list)
 