# Plotting performance of init_dict_.py scripts
# mean values with variances as error bars

import matplotlib.pyplot as plt

x = [1, 2, 3]

y_1 = [0.632433333333333,5.96236666666667,60.9595666666667]
y_2 = [0.528633333333333,5.1351,52.6026666666667]

y_1_err = [0.000138043333333333,0.0398697433333334,2.13196982333333] 
y_2_err = [0.000141293333333333,0.00739423000000004,0.358660123333335]

x_labels = ["n = 10^6", "n = 10^7", "n = 10^8"]

plt.figure()
plt.errorbar(x, y_1, yerr=y_1_err, fmt='-x')
plt.errorbar(x, y_2, yerr=y_2_err, fmt='-^')

plt.xticks(x, x_labels)
plt.xlim([0,4])
plt.xlabel('size n')
plt.ylabel('cpu time in sec')
plt.yscale('log')
plt.title('Dictionary initialization 1')
plt.legend(['init_dict_1.py', 'init_dict_2.py'], loc='upper left')

#plt.show()
plt.savefig(./init_dict_1.png')
