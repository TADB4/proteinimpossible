import copy
from queue import Queue
from code.classes.protein import Protein

class Breadthfirst:
    def __init__(self, data):
        self.data = data
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
        print("queue:, ", queue)
        queue.put("")
        
        states = set()
        
        while not queue.empty():
            state = queue.get()

            print("state", state)

            temp_state_list = state.split("/")

            print("temp state list: ", temp_state_list)

            if len(temp_state_list) >= depth:
                print("appending state", state)
                states.add(str(state))
                                                            #create starting molecule
            if len(state) < depth:

                # make copy of this state for each option
                for i in ['-2/', '-1/', '1/', '2/']:
                    child = copy.deepcopy(state)
                    child += i
                    queue.put(child)
        
        print("states:")
        for i in states:
            print(i)

    def try_fold_order(self):
        pass