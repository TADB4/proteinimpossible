from code.classes import protein, aminoacid
from code.visualisation import visualise
from code.algorithms import randomise, greedy, breadthfirst, breadthfirst_pruning
import copy
import csv
import time

if __name__ == "__main__":
    # ------------- Function for running random and greedy algorithm -------------
    def run_algorithm(algorithm, times):
        """
        Runs an algorithm x times and saves values needed for csv and visualisation export
        """
        start_time = time.time()
        best_stability = 0
        best_protein = None
        csv_all_scores = []

        # run random algorithm x times
        for counter in range(0, times):
            if algorithm == 'greedy':
                current_object = greedy.Greedy(data)
            else:
                current_object = randomise.Randomise(data)

            current_protein = current_object.protein
            protein.Protein.score(current_protein)
            csv_all_scores.append([current_protein.stability])

            # if this protein has the best score, overwrite previous best protein
            if int(current_protein.stability) < int(best_stability):
                best_stability = current_protein.stability
                best_protein = current_protein 
                print("New best score:", current_protein.stability)

        # make folds list for csv file
        csv_best_score = []
        csv_best_score.append(['amino', 'fold'])
        for aminoacid in best_protein.aminoacids:
            csv_best_score.append([aminoacid.nucleotide, aminoacid.fold])
        csv_best_score.append(['score', int(best_protein.stability)])

        print("Runtime: %s seconds" % (time.time() - start_time))

        return [best_protein, csv_best_score, csv_all_scores]

    # promt user for sequence
    data = str(input("Insert sequence here: "))
    
    # --------------------------- Random OR Greedy x times --------------------------
    a = input("What algorithm do you want to use? [randomise/greedy/breadthfirst] ")
    # ---------------------- run Random / Greedy ----------------------
    if a is 1 or 2:
        times = int(input("How many times do you want to run the algorithm? "))
        print("random greedy running")
        if a == 1:
            algorithm = 'randomise'
        else:
            algorithm = 'greedy'
        outputs = run_algorithm(algorithm, times)
        best_protein = outputs[0]
        csv_best_score = outputs[1]
        csv_all_scores = outputs[2]
    # ---------------------- run Breadth first ----------------------
    else:
        print("breadfirst running")
        start_time = time.time()
        current_object = breadthfirst_pruning.Breadthfirst(data)
        best_protein = current_object.protein
        csv_best_score = best_protein.csv_best_score
        csv_all_scores = current_object.csv_all_scores
        print("Runtime: %s seconds" % (time.time() - start_time))

    # ---------------------- Visualisation ----------------------
    visualise.make_plot(best_protein)
    visualise.write_csv_rows('results/output.csv', csv_best_score)
    visualise.write_csv_rows('results/all_scores.csv', csv_all_scores)



    # -------------------- Old versions Random and Greedy -----------   
    # start_time = time.time()
    # current_object = randomise.Randomise(data)
    # current_protein = current_object.protein
    # print("Runtime: %s seconds" % (time.time() - start_time))
    # protein.Protein.score(current_protein)
    
    # start_time = time.time()
    # current_object = greedy.Greedy(data)
    # current_protein = current_object.protein
    # print("Runtime: %s seconds" % (time.time() - start_time))
    # protein.Protein.score(current_protein)

    # ------------------- Old random 100k code ( x sofie, niet verwijderen) --------------
    # start_time = time.time()
    # best_stability = 0
    # best_protein = None
    # csv_all_scores = []

    

    # # run random algorithm x times
    # for counter in range(0, times):
    #     current_object = randomise.Randomise(data)
    #     current_protein = current_object.protein
    #     protein.Protein.score(current_protein)
    #     csv_all_scores.append([current_protein.stability])

    #     # if this protein has the best score, overwrite previous best protein
    #     if int(current_protein.stability) < int(best_stability):
    #         best_stability = current_protein.stability
    #         best_protein = current_protein 
    #         print("New best score:", current_protein.stability)

    # # make folds list for csv file
    # csv_best_score = []
    # csv_best_score.append(['amino', 'fold'])
    # for aminoacid in best_protein.aminoacids:
    #     csv_best_score.append([aminoacid.nucleotide, aminoacid.fold])
    # csv_best_score.append(['score', int(best_protein.stability)])

    # print("Runtime: %s seconds" % (time.time() - start_time))
