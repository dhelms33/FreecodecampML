import tensorflow as tf 
import numpy as np 
import matplotlib as plt

#linear regression
#life expectancy, algo finds magnitude
x = [1,2,2.5, 3, 4]
y = [1,4,7,9,15]
plt.plot(x,y,'ro') #plots data points, x,y as red, circles =o
plt.axis([0,6,0,20]) #plots the x axis domain as 0,6 and the range from 0 to 20
plt.plot(np.unique(x), np.ploy1d(np.polyfit(x,y,1),))((np.unique(x))) #np.unique returns the sorted unique values from the array, poly1d creates a polynomial 1d f(x), double parenth and ending unique statement take the unique x to calc y
plt.show()



#left off at 13:14