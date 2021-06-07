# class Visualision:
#     def __init__(self, protein)
#         self.protein = protein

# NOTE: install correct python version for matplotlib
# https://matplotlib.org/stable/faq/installing_faq.html

import matplotlib
import matplotlib.pyplot as plt 
from code.classes import protein, molecule

X_MIN = -10
X_MAX = 10
Y_MIN = -10
Y_MAX = 10

# print("test 2")

def make_plot(protein):
    # print("TEST3")
    # testdata
    protein = protein
    protein_dict = protein.occupied
    #print(protein_dict)
    # make plot
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)

    # Set title
    fig.suptitle('Protein representation', fontsize=14, fontweight='bold')

    # set x- and y-axis limits
    ax.axis([X_MIN, X_MAX, Y_MIN, Y_MAX])

    # loop over molecules of the protein
    for i, item in enumerate(protein_dict):
        # obtain x and y values
        item_list = protein_dict[i] #item.split(",")
        x_value = int(item_list[0])
        y_value = int(item_list[1])

        # print nucleotide at correct location
        ax.plot(x_value, y_value, protein_dict[i])

    # save figure
    plt.savefig("test")






