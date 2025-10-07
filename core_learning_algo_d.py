#load model in batches
#left off 7:10
#only load certain elements in batches
#epoches = how many times the data is going to see the same data
def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32): #why not a class?
    def input_function(): #inner function, this will be returned
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df, label_df)) # create tf.data.Dataset object with data
        if shuffle:
            ds = ds.shuffle(1000) # randomize
        ds = ds.batch(batch_size).repeat(num_epochs) # split dataset into batches of 32 and repeat process
        return ds #return a batch of the dataset
    return input_function
    
train_input_fn = make_input_fn(dftrain, y_train) # call input fn that was return to get a dataset
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs = 1, shuffle = False)

                                                