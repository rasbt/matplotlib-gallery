# Sebastian Raschka 01/26/2014

from read_iris_data import iris_data_to_arrays

import numpy as np
from matplotlib import pyplot as plt

def flower_scatterplots():

    setosa, versicolor, virginica = iris_data_to_arrays('./iris_data.txt')
    
    plt.figure(figsize=(15,15))
    
    plt.subplot(211)
    plt.scatter(setosa[0,:], setosa[1,:], marker='x', color='blue')
    plt.scatter(versicolor[0,:], versicolor[1,:], marker='o', color='green')
    plt.scatter(virginica[0,:], virginica[1,:], marker='^', color='red')
    plt.title('Sepal Length (x1) Vs. Sepal Width (x2)')
    plt.ylabel('Sepal width in cm')
    plt.xlabel('Sepal length in cm')
    plt.legend(['Setosa', 'Versicolor', 'Virginica'], loc='upper right')

    plt.subplot(212) 
    plt.scatter(setosa[0,:], setosa[3,:], marker='x', color='blue')
    plt.scatter(versicolor[0,:], versicolor[3,:], marker='o', color='green')
    plt.scatter(virginica[0,:], virginica[3,:], marker='^', color='red')
    plt.title('Sepal Length (x1) Vs. Petal Width (x4)')
    plt.ylabel('Petal width in cm')
    plt.xlabel('Sepal length in cm')
    plt.legend(['Setosa', 'Versicolor', 'Virginica'], loc='upper right')    
    
    plt.savefig('./flower_2d_scatter.png')

if __name__ == '__main__':
    flower_scatterplots()


