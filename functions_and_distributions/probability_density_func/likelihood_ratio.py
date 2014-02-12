# Sebastian Raschka, 2014
# Plotting the likelihood ratio of 2 probability density functions.


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

x = np.arange(0, 50, 0.05)

likelihood_ratio = pdf(x, mu=30, sigma=10**0.5) / pdf(x, mu=40, sigma=20**0.5)


plt.plot(x, likelihood_ratio)

plt.title('Likelihood ratio of 2 probability density functions')
plt.ylabel('p(x | w1) / p(x | w2)')
plt.xlabel('random variable x')

plt.figtext(.5,.85,'p(x|w1) ~ N(30,10), p(x|w2) ~ N(40,20)', fontsize=12, ha='center')

plt.savefig('./likelihood_ratio.png')
