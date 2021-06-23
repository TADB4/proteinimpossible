from code.classes import protein, aminoacid
from code.visualisation import visualise
from code.algorithms import randomise, greedy, breadthfirst, breadthfirst_pruning, depthfirst, depthfirst_pruning
import copy
import csv
import time

def main():
    # ---------------------- promt the user ----------------------
    # promt user for sequence
    while True:
        data = str(input("Insert sequence here: "))
        if not data.isupper():
            print("Please write sequence in uppercase.")
        else:
            break
    
    # promt user for algorithm
    while True:
        algorithm = input("What algorithm do you want to use? ")
        if algorithm not in ('randomise', 'greedy', 'breadthfirst', 'breadthfirst_pruning', 'depthfirst', 'depthfirst_pruning'):
            print("Please choose one of the options ('randomise', 'greedy', 'breadthfirst', 'breadthfirst_pruning', 'depthfirst', 'depthfirst_pruning') and write in lowercase.")
        else:
            break

    # ---------------------- run Random / Greedy ----------------------
    if algorithm == 'randomise' or algorithm == 'greedy':
        while True:
              times = input("How many times do you want to run the algorithm? ")
              if not times.isnumeric():
                  print("Please enter a number.")
              else:
                  times = int(times)
                  break
    
        print(algorithm, "is running..")
        outputs = run_algorithm(data, algorithm, times)
        best_protein = outputs[0]
        csv_best_score = outputs[1]
        csv_all_scores = outputs[2]
    
    # ---------------------- run Breadthfirst / Depthfirst ----------------------
    else:
        print(algorithm, "is running..")
        start_time = time.time()

        if algorithm == 'breadthfirst':
            current_object = breadthfirst.Breadthfirst(data)
        elif algorithm == 'breadthfirst_pruning':
            current_object = breadthfirst_pruning.Breadthfirst_pruning(data)
        elif algorithm == 'depthfist':
            current_object = depthfirst.Depthfirst(data)
        else:
            current_object = depthfirst_pruning.Depthfirst_pruning(data)

        best_protein = current_object.protein
        csv_best_score = best_protein.csv_best_score
        csv_all_scores = current_object.csv_all_scores
        print("Runtime: %s seconds" % (time.time() - start_time))
   
    # ---------------------- Visualisation of picture and csv files ----------------------
    visualise.make_plot('results/bestprotein', best_protein)
    visualise.write_csv_rows('results/output.csv', csv_best_score)
    visualise.write_csv_rows('results/all_scores.csv', csv_all_scores)

def run_algorithm(data, algorithm, times):
    """
    Runs an algorithm x times and returns values needed for csv and visualisation export
    """
    start_time = time.time()
    best_stability = 0
    best_protein = None
    csv_all_scores = []

    # run random algorithm variable amount of times
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
            tries_best = counter + 1
            time_to_find =  time.time() - start_time
            print("New best score:", current_protein.stability, ", try number:", tries_best, ", time to find:", time_to_find)

    # make folds list for csv file
    csv_best_score = []
    csv_best_score.append(['amino', 'fold'])

    # write data for best protein csv file
    for aminoacid in best_protein.aminoacids:
        csv_best_score.append([aminoacid.aminoacid_type, aminoacid.fold])
    csv_best_score.append(['score', int(best_protein.stability)])

    print("Runtime: %s seconds" % (time.time() - start_time))

    return [best_protein, csv_best_score, csv_all_scores]

if __name__ == "__main__":
    main()
    
    
    
