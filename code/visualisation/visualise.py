import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.lines as mlines
from code.classes import protein, molecule

def make_plot(protein):
    '''
    Visualisation code that plots a protein using matplotlib
    '''
    print("Loading visualisation...")

    protein_dict = protein.molecule_locations
    
    # make plot
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)

    # adjust graph size to length of the protein
    max_length = protein.size_data + 1

    # set title
    fig.suptitle('Protein representation', fontsize=14, fontweight='bold')

    # set x- and y-axis limits
    ax.axis([(-max_length), (max_length), (-max_length), (max_length)])

    x_values = []
    y_values = []

    for item in protein_dict:
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






