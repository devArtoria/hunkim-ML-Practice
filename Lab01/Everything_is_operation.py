
import tensorflow as tf

hello = tf.constant('hello Tensors!')

sess = tf.Session()

print (sess.run(hello))
print(hello)