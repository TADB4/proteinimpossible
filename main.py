from code.classes import protein, molecule
from code.visualisation import visualise
# from code.algorithms import randomise, greedy, hillclimber, antcolony
import csv
from statistics import mean

if __name__ == "__main__":
    # promt user for sequence
    data = str(input("Insert sequence here: "))
    # algorithm = str(input("Which algorithm would you like to use? "))
    times = int(input("How many times do you want to run the algorithm? "))

    csv_rows_baseline = []
    
    for protein_counter in range(0, times):
        csv_rows = []
        
        # add first line of output csv file
        csv_rows.append(['amino','fold'])

        # initialize protein class
        current_protein = protein.Protein(data)

        for loc in current_protein.occupied:
            # PROTEIN CHECK:
            # print(f"nucleotide: {molecule.nucleotide}, molecule number: {molecule.molecule_number}, fold: {molecule.next_fold}, location: {molecule.location}")
            
            molecule = current_protein.molecule_locations[tuple(loc)]
            
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
    visualise.write_csv_rows('results/baseline_scores.csv', csv_rows_baseline)

    # NIEUWE STRUCTUUR:
    # greedy roept protein aan (bijv geef volgende vouw opties functie)
    # protein roept molecule aan

    # in protein kan een rechte lijn met alleen protein volgorde gebouwd worden, en dat
    # de fold later wordt aangepast door een bepaald algoritme

    # houd de molecuul zo dat hij echt alleen de molecuul data kent







