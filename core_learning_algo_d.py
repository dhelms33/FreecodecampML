def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32): #why not a class?
    def input_function(): #inner function, this will be returned
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df, label_df)) # create tf.data.Dataset object with data