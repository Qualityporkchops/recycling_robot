import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import seaborn as sns
matplotlib.rcParams.update({'font.family': 'sans-serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'font.size':15
    })

dataset_url = 'C:/Users/Pierre/Documents/Programmation_icc/Python/Bottle'
data_dir = tf.keras.utils.get_file('Bottle', origin=dataset_url, untar=True)
data_dir = pathlib.Path(data_dir)

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)


