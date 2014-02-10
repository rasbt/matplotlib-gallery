# Sebastian Raschka, 2014
# Plotting the likelihood ratio of 2 probability density functions.


import numpy as np
from matplotlib import pyplot as plt
import math

def pdf(x, mean=0, std_dev=1):
    """Calculates the normal distribution's probability density 
        function (PDF).  
        
    """
    term1 = 1.0 / math.sqrt(2*np.pi) 
    term2 = np.exp( -0.5 * ( (x-mean)/std_dev )**2 )
    return term1 * term2

x = np.arange(0, 50, 0.05)

likelihood_ratio = pdf(x, mean=30, std_dev=10**0.5) / pdf(x, mean=40, std_dev=20**0.5)


plt.plot(x, likelihood_ratio)

plt.title('Likelihood ratio of 2 probability density functions')
plt.ylabel('p(x | w1) / p(x | w2)')
plt.xlabel('random variable x')

plt.figtext(.5,.85,'p(x|w1) ~ N(15,5), p(x|w2) ~ N(20,10)', fontsize=12, ha='center')

plt.savefig('./likelihood_ratio.png')
