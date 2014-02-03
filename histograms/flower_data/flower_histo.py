# Sebastian Raschka 01/21/2014

from read_iris_data import iris_data_to_arrays

import numpy as np
from matplotlib import pyplot as plt

def flower_histograms():

    setosa, versicolor, virginica = iris_data_to_arrays('./iris_data.txt')
    plt.figure(figsize=(15,15))
    #plt.subplots_adjust(hspace=0.1)
    plt.subplot(221)
    for flower in [setosa, versicolor, virginica]:
        bins = np.arange(4,8,0.1)
        plt.hist(flower[0,:], bins=bins, alpha=0.5)
    plt.ylim([0,15])
    plt.title('Sepal Length')
    plt.ylabel('Count')
    plt.xlabel('Sepal length in cm, bin size = 0.1 cm')
    plt.legend(['Setosa', 'Versicolor', 'Virginica'], loc='upper right')

    plt.subplot(222) 
    for flower in [setosa, versicolor, virginica]:
        bins = np.arange(1,5,0.1)
        plt.hist(flower[1,:], bins=bins, alpha=0.5)
    plt.ylim([0,15])
    plt.title('Sepal Width')
    plt.ylabel('Count')
    plt.xlabel('Sepal width in cm, bin size = 0.1 cm')
    plt.legend(['Setosa', 'Versicolor', 'Virginica'], loc='upper right')
    
    plt.subplot(223)    
    for flower in [setosa, versicolor, virginica]:
        bins = np.arange(0,8,0.2)
        plt.hist(flower[2,:], bins=bins, alpha=0.5)
    plt.ylim([0,25])
    plt.title('Petal Length')
    plt.ylabel('Count')
    plt.xlabel('Petal length in cm, bin size = 0.2 cm')
    plt.legend(['Setosa', 'Versicolor', 'Virginica'], loc='upper right')

    plt.subplot(224)
    for flower in [setosa, versicolor, virginica]:
        bins = np.arange(0,3,0.1)
        plt.hist(flower[3,:], bins=bins, alpha=0.5)
    plt.ylim([0,40])
    plt.title('Petal Width')
    plt.ylabel('Count')
    plt.xlabel('Petal width in cm, bin size = 0.1 cm')
    plt.legend(['Setosa', 'Versicolor', 'Virginica'], loc='upper right')

    plt.savefig('./flower_histo.png')

if __name__ == '__main__':
    flower_histograms()


