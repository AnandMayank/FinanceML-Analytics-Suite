import tensorflow as tf

# Set GPU as the device
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        # Set memory growth to avoid allocation issues
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        tf.config.set_visible_devices(gpus, 'GPU')
        print("Running on GPU")
    except RuntimeError as e:
        print(e)
else:
    print("No GPU detected, running on CPU.")
