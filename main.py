from code.classes import protein, aminoacid
from code.visualisation import visualise
from code.algorithms import randomise, greedy, breadthfirst
import copy
import csv
import time

if __name__ == "__main__":
    # promt user for sequence
    data = str(input("Insert sequence here: "))

    algorithm = "breadthfirst"
   
    times = int(input("How many times do you want to run the algorithm? "))

    csv_rows_baseline = []
    highest_stability = 1
    
    start_time = time.time()

    for protein_counter in range(0, times):

        # print at every 100 proteins
        if protein_counter%100 == 0:
            print("Making protein nr", protein_counter)
            print("Runtime: %s seconds" % (time.time() - start_time))

        # execute random/greedy/breadthfirst algorithm
        if algorithm == "randomise":
            random_object = randomise.Randomise(data)
            current_protein = random_object.protein
        elif algorithm == "greedy":
            greedy_object = greedy.Greedy(data)
            current_protein = greedy_object.protein
        elif algorithm == "breadthfirst":
            breadthfirst_object = breadthfirst.Breadthfirst(data)
            current_protein = breadthfirst_object.protein

        # count score
        #print("calculate score...")
        protein.Protein.score(current_protein)
        #print("stability: ", current_protein.stability)
        
        # make csv rows and add first line of output csv file
        csv_rows = []
        csv_rows.append(['amino','fold'])
        
        # loop over aminoacids
        for aminoacid in current_protein.aminoacids:
            # PROTEIN CHECK:
            # print(f"nucleotide: {aminoacid.nucleotide}, aminoacid number: {aminoacid.aminoacid_number}, fold: {aminoacid.next_fold}, location: {aminoacid.location}")
            
            # add aminoacids and folds to csv rows
            csv_rows.append([aminoacid.nucleotide, aminoacid.fold])

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
            file_name = 'results/output.csv'
            visualise.write_csv_rows(file_name, csv_rows)

            highest_stability = copy.deepcopy(current_protein.stability)

    # export csv file for baseline results
    visualise.write_csv_rows('results/baseline_scores.csv', csv_rows_baseline)







