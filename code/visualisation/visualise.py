# class Visualision:
#     def __init__(self, protein)
#         self.protein = protein

# NOTE: install correct python version for matplotlib
# https://matplotlib.org/stable/faq/installing_faq.html

import matplotlib
import matplotlib.pyplot as plt 

X_MIN = -10
X_MAX = 10
Y_MIN = -10
Y_MAX = 10

print("test 2")

def make_plot(protein):
    print("TEST3")

    # make plot
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)

    # Set title
    fig.suptitle('Protein representation', fontsize=14, fontweight='bold')

    # set x- and y-axis limits
    ax.axis([X_MIN, X_MAX, Y_MIN, Y_MAX])

    # print something
    ax.plot([0], [0], 'H')

    # show plot
    plt.show()






