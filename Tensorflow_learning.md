[动态申请显存](https://www.jianshu.com/p/5d47f152ff62)

    config = tf.ConfigProto()  
    config.gpu_options.allow_growth = True  
    session = tf.Session(config=config)
