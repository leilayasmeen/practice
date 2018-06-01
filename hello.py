import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
gpu_config = tf.ConfigProto()
gpu_config.gpu_options.visible_device_list = str(2)
sess = tf.Session(config=gpu_config) 
sess.run(hello)