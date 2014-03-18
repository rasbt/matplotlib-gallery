# Sebastian Raschka, 03/2014 

import numpy as np
import matplotlib.pyplot as plt

def eval_sample_cat(sample_counts, key, val):
    """
    Expects a sample_counts dict from read_csv_barplot().
    Increases the respective count in the dictionary.
    
    """
    sample_counts[key][int(val)-1] += 1

def read_csv(file_loc):
    """
    Evaluates a csv file that contains ranked metrics.    
    Keyword arguments:
        file_loc (str): path to the csv file
            Expected file format, e.g.,
            
                label,var1,var2,var3
                sample1,1,3,2
                sample2,3,2,1
                sample3,2,1,3      

    Returns a dictionary with counts of the sample category performace, where
    the 1st item in the sublists means that the sample category (here: the key)
    performed x-times best (2nd item means x-times second best, etc.)
        E.g., 
        {'var3': [14, 7, 1], 'var1': [9, 5, 8], 'var2': [9, 7, 6]}
    
    """
    with open(file_loc, 'r') as in_data:
        header = in_data.readline().strip().split(',')
        # expected header: ['label', 'var1', 'var2', 'var3']
        sample_counts = {header[1]:[0,0,0], header[2]:[0,0,0], header[3]:[0,0,0]}
        for line in in_data:
            if line and not line.startswith('#'): # skip comments and blank lines
                line = line.strip().split(',')
                for i in range(1,4):
                    eval_sample_cat(sample_counts, header[i], line[i])
    return sample_counts           
            
def plot_barplot(sample_counts):
    """ Plotting the grouped bar plot from the sample_counts dictinary """
    N = len(sample_counts.keys())
    ind = np.arange(N)  # the x locations for the groups
    width = 0.2       # the width of the bars
    
    fig, ax = plt.subplots()
    
    labels = []
    data_points = []
    for k in sample_counts.keys():
        labels.append(k)
        data_points.append(sample_counts[k])
      
    plt.bar(ind, [d[0] for d in data_points], width,
                 alpha=0.5,
                 color='g',
                 label=labels[0])

    plt.bar(ind + width, [d[1] for d in data_points], width,
                 alpha=0.5,
                 color='b',
                 label=labels[1])
    
    plt.bar(ind + 2*width, [d[2] for d in data_points], width,
                 alpha=0.5,
                 color='r',
                 label=labels[2])
    
    ax.set_ylabel('Count')
    ax.set_title('Metrics to predict best docking ligand conformation and orientation')
    ax.set_xticks(ind + 1.5 * width)
    ax.set_xticklabels(labels)
    plt.xlim(-0.5,3)
    plt.ylim(0,15)
    plt.legend(['best', '2nd best', '3rd best'], loc='upper left')
    plt.show()
    
data_file = './twelve_samples_ranks.csv'    
sample_counts = read_csv(data_file)
print(sample_counts)
plot_barplot(sample_counts)
