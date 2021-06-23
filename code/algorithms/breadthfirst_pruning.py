import copy
from queue import Queue
from code.classes.protein import Protein
from code.algorithms.constructive_tool import Constructive_tool

"""
Works the same as the breadthfirst class but prunes impossible fold orders 
and only saves half of the results to reduce memory costs
"""
class Breadthfirst_pruning(Constructive_tool):
    def __init__(self, data):
        super().__init__(data)

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
                        if order in str(child):
                            good_order = False

                    # if no impossible fold orders are possible, add to queue     
                    if good_order == True:
                        queue.put(child + ",")
            else:
                # for the complete state lists, only add halve 
                if (x % 2) == 0:       
                    self.states.append(state_list)
            
            x = x + 1
                