#dfeval.shape
#(264,9)
#typically have testing and training data
import tensorflow as tf 
import tensorflow.compat.v2.feature_column as fc 
import pandas as pd 

dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/tianic/train.csv') #training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/tianic/train.csv')
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class','deck', 'embark_town', 'alone']

NUMERIC_COLUMNS = ['age','fare']

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
    vocabulary = dftrain[feature_name].unique() #gets a list of all unique values from given feature to give to our model to make predictions
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
    feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))
    
print(feature_columns)

#commands being run to get unique values
#dftrain["sex"].unique
#dftrain["embark_town"].unique()

#linear regression needs all vocabs


