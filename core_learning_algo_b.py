import tensorflow as tf 
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib as plt
fromIPython.display import clear_output
from six.moves import urllib
#stopped at 5:17
#load dataset
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') #loads titanic dataset into pandas DataFrame
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') #loads the testing dataset into a DataFrame, used to evaluate model after training
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

#use dftrain.head() to show first 5 items in DataFrame
dftrain.head()

#for a more statisitical analysis of or data, we use .describe()
dftrain.describe()

#we also should know the shape of the data as well
dftrain.shape
