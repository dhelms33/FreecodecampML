#dfeval.shape
#(264,9)
#typically have testing and training data
import tensorflow as tf 
import tensorflow.compat.v2.feature_column as fc 
import pandas as pd 

dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/tianic/train.csv') #training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/tianic/train.csv')
CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class','deck', 'embark_town', 'alone']
