import copy
from code.classes.protein import Protein
from code.algorithms.tool import Tool

"""
Class containing functions that are used by the constructive algorithms(Breadthfirst and Depthfirst)
"""
class Constructive_alg_tool:
    def __init__(self, data):
        self.data = data
        self.data = data
        self.states = []
        self.csv_all_scores = []
        self.protein = Protein(data)
        self.potential_fold_order()
        self.try_every_fold()  

    def apply_fold(self, current_location, state, csv_rows):
        """
        Applies the fold for all states
        """
        for i, aminoacid in enumerate(self.protein.aminoacids):
            
            # set location that is calculated with previous fold
            aminoacid.location = current_location
            self.protein.occupied[i] = copy.deepcopy(current_location)

            fold = state[i]

            # add fold to csv output file
            csv_rows.append([aminoacid.aminoacid_type, fold])
        
            # calculate future location with this fold
            future_location = Tool.assign_location(self.protein, current_location, fold)
            
            # if location is free, fold aminoacid and update information
            if future_location not in self.protein.occupied:
                aminoacid.fold = fold
                current_location = future_location
            else:
                break  

    def try_every_fold(self):
        """
        Tests all states of folding
        """
        # possible_proteins = []
        best_stability = 0
        best_protein = None

        # loop over every state of states
        for state in self.states:
            # make a protein without folds
            self.protein = Protein(self.data)
            
            # start location
            current_location = [0,0]

            # start csv output file
            csv_rows = []
            csv_rows.append(['amino','fold'])
            
            self.apply_fold(current_location, state, csv_rows)

            # calculate stability
            self.protein.stability = self.protein.score()

            # add score to csv rows
            csv_rows.append(['score', self.protein.stability])

            # save score of this protein to the big csv file
            self.csv_all_scores.append([self.protein.stability])

            # if this protein has the best score, overwrite previous best protein
            if int(self.protein.stability) < int(best_stability):
                best_protein = self.protein
                best_stability = self.protein.stability
                self.protein.csv_best_score = csv_rows
                print("New best score:", self.protein.stability)
            
        # return the protein with the highest score
        self.protein = best_protein