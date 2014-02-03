# Sebastian Raschka 01/26/2014

from read_iris_data import iris_data_to_arrays
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt

def flower_3d_scatterplot():

    setosa, versicolor, virginica = iris_data_to_arrays('./iris_data.txt')
    
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111, projection='3d')
   
    ax.scatter(setosa[0,:], setosa[1,:], setosa[3,:], marker='x', color='blue')
    ax.scatter(versicolor[0,:], versicolor[1,:], versicolor[3,:], marker='o', color='green')
    ax.scatter(virginica[0,:], virginica[1,:], virginica[3,:], marker='^', color='red')

    ax.set_xlabel('Sepal Length')
    ax.set_ylabel('Sepal Width')
    ax.set_zlabel('Petal Width')

    plt.title('Sepal Length (x1) Vs. Sepal Width (x2) Vs. Petal Width (x4)')
     
    #plt.savefig('./flower_3d_scatter.png')
    plt.show()

if __name__ == '__main__':
    flower_3d_scatterplot()


