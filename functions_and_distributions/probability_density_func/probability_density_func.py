# Sebastian Raschka, 2014
# Plotting Probability Density Functions

import numpy as np
from matplotlib import pyplot as plt
import math

def pdf(x, mu=0, sigma=1):
    """Calculates the normal distribution's probability density 
        function (PDF).  
        
    """
    term1 = 1.0 / ( math.sqrt(2*np.pi) * sigma )
    term2 = np.exp( -0.5 * ( (x-mu)/sigma )**2 )
    return term1 * term2


x = np.arange(0, 100, 0.05)

pdf1 = pdf(x, mu=5, sigma=2.5**0.5)
pdf2 = pdf(x, mu=10, sigma=6**0.5)

plt.plot(x, pdf1)
plt.plot(x, pdf2)
plt.title('Probability Density Functions')
plt.ylabel('p(x)')
plt.xlabel('random variable x')
plt.legend(['pdf1 ~ N(5,2.5)', 'pdf2 ~ N(10,6)'], loc='upper right')
plt.ylim([0,0.5])
plt.xlim([0,20])

plt.savefig('./probability_density_func.png')
