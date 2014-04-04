# Sebastian Raschka 01/21/2014
#
# Functions to read in the data set

import numpy as np

def iris_data_to_arrays(file_loc):
    """Reads in data from the iris_data.txt data set.
    
    Keyword Arguments:
        file_loc (str): location of the data file

    """
    all_data = np.genfromtxt(file_loc)

    # each row consists of a measurements with the features:
    # [sepal_length, sepal_width, petal_length, petal_width, flower_class]

    #>>> all_data
    #array([[ 5.1,  3.5,  1.4,  0.2,  1. ],
    #   [ 4.9,  3. ,  1.4,  0.2,  1. ],
    # ...

    setosa = all_data[all_data[:,4] == 1]
    versicolor = all_data[all_data[:,4] == 2]
    virginica = all_data[all_data[:,4] == 3]

    setosa = setosa[:,0:4].T
    versicolor = versicolor[:,0:4].T
    virginica = virginica[:,0:4].T

    # Transposed into:
    # [s_len, s_len, s_len, ...],
    # [s_wid, s_wid, s_wid, ...],
    # [p_len, p_len, p_len, ...],
    # [p_wid, p_wid, p_wid, ...],

    assert setosa.shape == (4,50)
    assert versicolor.shape == (4,50)
    assert virginica.shape == (4,50)

    return setosa, versicolor, virginica

if __name__ == '__main__':
    setosa, versicolor, virginica = iris_data_to_arrays('./iris_data.txt')
    

