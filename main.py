from code.classes import protein, molecule
from code.visualisation import visualise
import csv
from statistics import mean

if __name__ == "__main__":
    # promt user for sequence
    data = str(input("Insert sequence here: "))
    times = int(input("How many tries? "))

    csv_rows_baseline = []
    
    for protein_counter in range(0, times):
        csv_rows = []
        
        # add first line of output csv file
        csv_rows.append(['amino','fold'])

        # initialize protein class
        current_protein = protein.Protein(data)

        # TEST: print each nucleotide and details
        for molecule in current_protein.molecules:
            #print(f"nucleotide: {molecule.nucleotide}, molecule number: {molecule.molecule_number}, fold: {molecule.next_fold}, location: {molecule.location}")

            # add aminoacids and folds to csv rows
            csv_rows.append([molecule.nucleotide, molecule.next_fold])

        # print(f"stability: {current_protein.stability}")

        # add score to csv rows
        csv_rows.append(['score', current_protein.stability])

        # add score to baseline csv file
        csv_rows_baseline.append([current_protein.stability])

        # make output csv file
        file_name = 'results/output_file' + str(protein_counter) + '.csv'
        visualise.write_csv_rows(file_name, csv_rows)

        visualise.make_plot(current_protein, protein_counter)
    
    # export csv file for baseline results
    file_name = 'results/baseline_scores.csv'
    visualise.write_csv_rows(file_name, csv_rows_baseline)






