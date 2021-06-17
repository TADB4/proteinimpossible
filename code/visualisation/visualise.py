import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.lines as mlines
from code.classes import protein, aminoacid
import csv

def calculate_axis(protein):
    """
    Calculates the minimum and maximum score of x and y to correctly adjust the size of the plot
    """
    x_min, x_max, y_min, y_max = 0, 0, 0, 0

    # remember the highest and lowest x and y values
    for item in protein.occupied:
        if item[0] < x_min:
            x_min = item[0]
        if item[0] > x_max:
            x_max = item[0]
        if item[1] < y_min:
            y_min = item[1]
        if item[1] > y_max:
            y_max = item[1]

    x_min -=2
    x_max +=2
    y_min -=2
    y_max +=2

    return [x_min, x_max, y_min, y_max]

def make_plot(protein, protein_counter):
    """
    Visualisation code that plots a protein using matplotlib
    """
    
    print("loading csv...")

    # make plot
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.85)

    # set title
    fig.suptitle('Protein representation', fontsize=14, fontweight='bold')

    # set x- and y-axis limits
    axes = calculate_axis(protein)
    ax.axis(axes)

    x_values = []
    y_values = []

    for i, item in enumerate(protein.occupied):
        # obtain x and y values to remember for lines
        x_value = int(item[0])
        y_value = int(item[1])

        # print nucleotide at correct location with correct color
        if protein.aminoacids[i].nucleotide == "H":
            ax.plot(x_value, y_value, 'bo')
        elif protein.aminoacids[i].nucleotide == "P":
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

    # print score in the left down corner
    ax.text(axes[0] + 1, axes[2] + 1, (f'score: {protein.stability}'))

    # remove axes
    # ax.axis('off')

    # save with unique file name
    # file_location = 'results/test_' + str(protein_counter)

    # save with best file name (overwrite last best protein)
    file_location = 'results/best'

    # save figure
    plt.savefig(file_location)

def write_csv_rows(file_name, rows):

    # open file in write mode
    with open(file_name, 'w', newline='') as f:

        # create csv writer
        writer = csv.writer(f)

        # write row to the file
        writer.writerows(rows)







