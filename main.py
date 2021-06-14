from code.classes import protein, molecule
from code.visualisation import visualise
from code.algorithms import randomise, greedy
import copy
import csv

if __name__ == "__main__":
    # promt user for sequence
    data = str(input("Insert sequence here: "))
    # algorithm = str(input("Which algorithm would you like to use? [none, randomise, greedy, hillclimber] "))
    times = int(input("How many times do you want to run the algorithm? "))

    csv_rows_baseline = []
    highest_stability = 0
    
    for protein_counter in range(0, times):

        # initialize protein class

        """
         # Greedy
        greedy_object = greedy.Greedy(data)
        current_protein = greedy_object.protein
        """
        # Random
        random_object = randomise.Randomise(data)
        current_protein = random_object.protein
        
        # make csv rows and add first line of output csv file
        csv_rows = []
        csv_rows.append(['amino','fold'])
        
        # loop over molecules
        for molecule in current_protein.molecules:
            # PROTEIN CHECK:
            # print(f"nucleotide: {molecule.nucleotide}, molecule number: {molecule.molecule_number}, fold: {molecule.next_fold}, location: {molecule.location}")
            
            # add aminoacids and folds to csv rows
            csv_rows.append([molecule.nucleotide, molecule.fold])

        # add score to csv rows
        csv_rows.append(['score', current_protein.stability])

        # add score to baseline csv file
        csv_rows_baseline.append([current_protein.stability])

        # # make output csv file (unique for this protein)
        # file_name = 'results/output_file' + str(protein_counter) + '.csv'
        # visualise.write_csv_rows(file_name, csv_rows)

        # save csv and plot if this protein has the highest score so far
        if int(current_protein.stability) < int(highest_stability):
            # make the protein visualisation plot
            visualise.make_plot(current_protein, protein_counter)

            # make output csv file 
            file_name = 'results/output_best.csv'
            visualise.write_csv_rows(file_name, csv_rows)

            highest_stability = copy.deepcopy(current_protein.stability)

    # export csv file for baseline results
    visualise.write_csv_rows('results/baseline_scores.csv', csv_rows_baseline)







