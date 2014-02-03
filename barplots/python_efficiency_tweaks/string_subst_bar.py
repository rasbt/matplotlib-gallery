# Plotting performance of string_subst_.py scripts
# bar chart of relative comparison with variances as error bars

import numpy as np
import matplotlib.pyplot as plt

performance = [10.3882388499416,1,10.3212281215746]
variance = [0.790435196936213,0,0.827207394592818]
scripts = ['string_subst_1.py', 'string_subst_2.py', 'string_subst_3.py']

x_pos = np.arange(len(scripts))

plt.bar(x_pos, performance, yerr=variance, align='center', alpha=0.5)
plt.xticks(x_pos, scripts)
plt.axhline(y=1, linestyle='--', color='black')
plt.ylim([0,12])

plt.ylabel('rel. performance gain')
plt.title('String substitution - Speed improvements')

#plt.show()
plt.savefig('./string_subst_bar.png')
