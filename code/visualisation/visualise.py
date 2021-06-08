# class Visualision:
#     def __init__(self, protein)
#         self.protein = protein

# NOTE: install correct python version for matplotlib
# https://matplotlib.org/stable/faq/installing_faq.html

import matplotlib
import matplotlib.pyplot as plt 
from code.classes import protein, molecule


X_MIN = -5
X_MAX = 5
Y_MIN = -5
Y_MAX = 5

# print("test 2")

def make_plot(protein):
    protein = protein
    protein_dict = protein.molecule_locations
    
    # make plot
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)

    # TEST INFO - remove later
    # print("mol_loc", protein_dict)
    # for i, item in enumerate(protein_dict):
    #     print("item", item) # geeft (0,0)
    #     print("nucl", protein_dict[item].nucleotide) # geeft H

    # set title
    fig.suptitle('Protein representation', fontsize=14, fontweight='bold')

    # set x- and y-axis limits
    ax.axis([X_MIN, X_MAX, Y_MIN, Y_MAX])

    # remember location of last dot
    # last_dot = []

    x_values = []
    y_values = []

    # loop over molecules of the protein
    for i, item in enumerate(protein_dict):
        # remember location of last dot
        last_dot = item

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

        # print line between this dot and the one before
        # DOES NOT WORK
        # x_lines = [last_dot[0], item[0]]
        # y_lines = [last_dot[1], item[1]]
        # print("x lines", x_lines)
        # print("y lines", y_lines)
        # ax.plot(x_lines, y_lines)

        x_values.append(x_value)
        y_values.append(y_value)
    
    # print lines
    ax.plot(x_values, y_values)

    # save figure
    plt.savefig("test")






