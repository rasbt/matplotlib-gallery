# Sebastian Raschka, 03/2014

import numpy as np
import matplotlib.pyplot as plt

def read_csv_(file_loc):
    """
    Evaluates a csv file that contains some values for different
    category labels.

    Keyword arguments:
        file_loc (str): path to the csv file
            Expected file format, e.g.,
            
            label,var1,var2,var3
            sample1,2.5,3.6,2.7
            sample2,2.6,0.6,0.3
            sample3,2.3,1.2,2.9
            sample4,4.1,1.6,2.7        
    
    Returns 4 lists that contain the labels, var1_vals, var2_vals, var3_vals,
    
    """
    with open(file_loc, 'r') as in_data:
        header = in_data.readline().strip().split(',')
        # expected header: ['label', 'var1', 'var2', 'var3']
        labels = []
        var1 = []
        var2 = []
        var3 = []

        for line in in_data:
            if line.strip() and not line.startswith('#'): # skip comments and blank lines
                line = line.strip().split(',')
                print('line: ',line)
                labels.append(line[0])
                var1.append(float(line[1]))
                var2.append(float(line[2]))
                var3.append(float(line[3]))                
    return labels, var1, var2, var3  

def plot_rmsdplot(labels, var1, var2, var3):
    """ Plotting the grouped bar plot from the label_counts dictinary """
    N = len(labels)
    ind = np.arange(N)  # the x locations for the groups
    width = 1           # the width of the bars
    
    fig, ax = plt.subplots()
    
    # plot annotations
    ax.set_ylabel('labels')
    ax.set_xlabel('X')
    ax.set_title('categoric scatterplot with mean values')
    ax.set_yticks(ind + width)
    ax.set_yticklabels(labels)
    
    # scatterplots
    plt.scatter(var1, ind, color='r', alpha=0.5, marker='x', s=40)
    plt.scatter(var2, ind, color='b', alpha=0.5, marker='^', s=40)
    plt.scatter(var3, ind, color='g', alpha=0.5, marker='o', s=40)
    
    # plotting mean values
    plt.axvline(np.mean(var1), color='r', alpha=0.8, linestyle=':', linewidth=2)
    plt.axvline(np.mean(var2), color='g', alpha=0.8, linestyle=':', linewidth=2)
    plt.axvline(np.mean(var3), color='b', alpha=0.8, linestyle=':', linewidth=2)

    # dimensions and legend
    plt.xlim(-1,12)
    plt.ylim(-1, N+1)
    plt.legend(['s1 mean', 's2 mean', 's3 mean'] + labels, loc='upper right')
    plt.show()

data_file = './twelve_samples.csv'    
labels, var1, var2, var3 = read_csv_(data_file)
plot_rmsdplot(labels, var1, var2, var3)
