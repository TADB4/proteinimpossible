# class Visualision:
#     def __init__(self, protein)
#         self.protein = protein

# NOTE: install correct python version for matplotlib
# https://matplotlib.org/stable/faq/installing_faq.html

import matplotlib
import matplotlib.pyplot as plt 
from code.classes import protein, molecule

# print("test 2")

def make_plot(protein):
    protein = protein
    protein_dict = protein.molecule_locations
    
    # make plot
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)

    # adjust graph size to length of the protein
    max_length = protein.size_data + 1

    # TEST INFO - remove later
    # print("mol_loc", protein_dict)
    # for i, item in enumerate(protein_dict):
    #     print("item", item) # geeft (0,0)
    #     print("nucl", protein_dict[item].nucleotide) # geeft H

    # set title
    fig.suptitle('Protein representation', fontsize=14, fontweight='bold')

    # set x- and y-axis limits
    ax.axis([(-max_length), (max_length), (-max_length), (max_length)])

    x_values = []
    y_values = []

    # loop over molecules of the protein
    for i, item in enumerate(protein_dict):

        # obtain x and y values
        x_value = int(item[0])
        y_value = int(item[1])

        # print nucleotide at correct location with correct color
        if protein_dict[item].nucleotide == "H":
            ax.plot(x_value, y_value, 'bo')
        elif protein_dict[item].nucleotide == "P":
            ax.plot(x_value, y_value, 'ro')
        else:
            ax.plot(x_value, y_value, 'go')

        x_values.append(x_value)
        y_values.append(y_value)
    
    # print lines
    ax.plot(x_values, y_values)

    # save figure
    plt.savefig("test")






