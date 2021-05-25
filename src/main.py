#!./bin/python
import matplotlib.pyplot as plt
import numpy as np
import os
import re
import shutil
import string
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import preprocessing
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization

batch_size=32
seed=42

raw_train_ds = tf.keras.preprocessing.text_dataset_from_directory('dataset/',
                                                                  batch_size=batch_size,
                                                                  validation_split=0.2,
                                                                  subset='training',
                                                                  seed=seed)