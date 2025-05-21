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
#takes y_train and store it there

#use dftrain.head() to show first 5 items in DataFrame
dftrain.head()
print(dftrain.head())

#for a more statisitical analysis of or data, we use .describe()
dftrain.describe() #also returns 

#data is a binary representation of whether someone survide or not
#locating row
print(dftrain[0], y_trtrain.loc[0])
#locating row

print(dftrain[0], y_trtrain.loc[0])

#get age values
print(dftrain["age"]) #age column


#we also should know the shape of the data as well
dftrain.shape
#627, 9 features

#get histogram of age
dftrain.age.hist(bins=20)

#print sex calues
print(dftrain.sex.value_counts().plot(kind = 'barh'))

#print class values
print(dftrain['class'].value_counts().plot(kind='barh'))

#print survival rate
print(pd.concat([dftrain, y_train], axis =1).groupby('sex').survived.mean().plot(kind='barh').set_xlabel('% survive'))