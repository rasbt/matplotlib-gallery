# Sebastian Raschka, 02/2014


import numpy as np
from matplotlib import pyplot as plt

def read_methyl_data(csv_file):
    """ 
    Reads in data from a csv file and separates datapoints into 2 classes.
    
    Keyword Arguments:
        csv_file (str): path to the csv file to read.

    Returns:    
        id_dict: A dictionary that has IDs from column 1 as keys and the count
                 as values.
        methyl_charges: A list of the floats (column 4) that contains
                 the methyl charges.
        methylene_charges: A list of the floats (column 4) that contains
                 the methylene charges.
 
    """
    with open (csv_file,'rb') as csv:
        all_data = np.genfromtxt(csv, dtype=None, delimiter=',')
    
    # all_data is an array of form
    #    [(b'ZINC00043096', b'C.3', b'C2', 0.0638, b'methylene')
    #    (b'ZINC00043096', b'C.3', b'C4', 0.0669, b'methylene')
    #    (b'ZINC00090377', b'C.3', b'C7', 0.207, b'methyl') ...]

    methyl_charges = []
    methylene_charges = []
    id_dict = {}

    for row in all_data:
        
        if row[0] not in id_dict:
            id_dict[row[0]] = 1
        else:
            id_dict[row[0]] += 1

        if row[4] == b'methyl':
            methyl_charges.append(row[3])
        elif row[4] == b'methylene':
            methylene_charges.append(row[3])
                
    return id_dict, methyl_charges, methylene_charges
    

def plot_histogram(methyl_list, methylene_list, id_dict):
    
    plt.figure(figsize=(15,15))
    bins = np.arange(-1.1,1.0,0.01)
    ftext = 'ZINC compounds: {}\nMethyl groups: {}\nMethylene groups: {}\n'\
            .format(len(id_dict), len(methyl_list), len(methylene_list))
    plt.figtext(.2,.8, ftext, fontsize=14, ha='left')
    plt.xlim([-1.1,1.0])
    plt.ylim([0,25])
    plt.hist(methyl_list, bins=bins, alpha=0.5)
    plt.hist(methylene_list, bins=bins, alpha=0.5)
    plt.title('Methyl Vs. Methylene charges in ZINC compounds')
    plt.ylabel('Count')
    plt.xlabel('ZINC AMSOL charge')
    plt.legend(['methyl-group', 'methylene-group'], loc='upper right')
    plt.savefig('./methyl_charges.png')

if __name__ == '__main__':

    id_dict, methyl_charges, methylene_charges = read_methyl_data('./methyl_charges.csv')
    plot_histogram(methyl_charges, methylene_charges, id_dict)
