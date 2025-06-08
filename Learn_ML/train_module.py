# Import required libraries
# Install numpy, tensorflow, and maltiplotlib if not already installed
import os
import numpy as np
import tensorflow as tf  # type: ignore
from tensorflow import keras  # type: ignore
from tensorflow.keras.processing.image import ImageDataGenerator  # type: ignore
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout  # type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping  # type: ignore
from matplotlib import pyplot as plt  # type: ignore

# set random seed for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

# Dfine the constant value
IMAGE_SIZE = (256, 256)  # Size of the input images
BATCH_SIZE = 32  # Number of images to process in a batch
EPOCHS = 10  # Number of epochs to train the model
NUM_CLASSES = 2  # Number of output classes for the crops(healthy and diseased)
ANIMAL_CLASSES = 3  # Number of Animal classes (cat, dog and human)

# define the dataset directory and the model save path
DATASET_DIR = "Learn_ML"  # Directory containing the dataset
MODEL_SAVE_PATH = "rokie_model.h5"  # Path to save the trained model
