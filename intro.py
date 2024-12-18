import tensorflow as tf
print(tf.version)

string = tf. Variable("this is a string," tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.564, tf.float64)

rank1_tensor= tf.Variable(["Test", "Dereck"], tf.string)
rank2_tensor = tf.Variable(["test", "ok"], ["test", "yes"], tf.string)
rank3_tensor = tf.Variable(["Okay"], ["Okay"], ["Okay"])

tf.rank(rank2_tensor)

rank2_tensor.shape

tensor1 = tf.ones([1,2,3]) #one interior list, two lists inside of that list, each with three elements
tensor2 = tf.reshape(tensor1, [2,3,1])
tensor2 = tf.reshape(tensor1, [3,-1])

#types of tesnors: variables, constant, placeholder, sparsetensor
#all are immutable except variables

#evaluating tensors

with tf.Session() as sess: #get value of tensor
    tensor.eval()
    
t = tf.zeroes(5,5,5,5) #or t = tf.zeroes
print(t)
t = tf.reshape(t, [625])
t = tf.reshape(t, -1)