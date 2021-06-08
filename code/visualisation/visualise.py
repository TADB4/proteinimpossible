# class Visualision:
#     def __init__(self, protein)
#         self.protein = protein

# NOTE: install correct python version for matplotlib
# https://matplotlib.org/stable/faq/installing_faq.html

import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.lines as mlines
from code.classes import protein, molecule

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

        # remember x and y values
        x_values.append(x_value)
        y_values.append(y_value)
    
    # print connecting lines
    ax.plot(x_values, y_values, color='grey')

    # add legend
    blue = mlines.Line2D([], [], color='blue', marker='o',
            markersize=10, label='H')
    red = mlines.Line2D([], [], color='red', marker='o',
            markersize=10, label='P')
    green = mlines.Line2D([], [], color='green', marker='o',
            markersize=10, label='C')
    ax.legend(handles=[blue, red, green])

    # remove axes
    ax.axis('off')

    # save figure
    plt.savefig("test")






