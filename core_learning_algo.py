import tensorflow as tf 
import numpy as np 
import matplotlib as plt

#linear regression

x = [1,2,2.5, 3, 4]
y = [1,4,7,9,15]
plt.plot(x,y,'ro')
plt.axis([0,6,0,20])
plt.plot(np.unique(x), np.ploy1d(np.polyfit(x,y,1),))((np.unique(x)))
plt.show()

#left off at 4:16