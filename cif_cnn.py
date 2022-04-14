import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import numpy as np
import matplotlib.pyplot as plt

(X_train, y_train_), (X_test, y_test_) = datasets.cifar10.load_data()
X_train.shape