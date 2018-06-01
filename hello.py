import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

hello = tf.constant('Hello, TensorFlow!')
gpu_config = tf.ConfigProto()
gpu_config.gpu_options.visible_device_list = str(2)
sess = tf.Session(config=gpu_config) 
print(sess.run(hello))