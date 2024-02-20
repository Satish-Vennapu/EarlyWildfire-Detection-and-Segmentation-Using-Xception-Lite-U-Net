

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

from plotdata import plot_confusion_matrix
from config import Config_classification
from config import new_size

batch_size = Config_classification.get('batch_size')
image_size = (new_size.get('width'), new_size.get('height'))
epochs = Config_classification.get('Epochs')


#########################################################
# Function definition

def classify():
    """
    This function load the trained model from the previous task and evaluates the performance of that over the test
    data set.
    :return: None, Plot the Confusion matrix for the test data on the binary classification
    """
    test_ds = tf.keras.preprocessing.image_dataset_from_directory(
        "frames/Test", seed=1337, image_size=image_size, batch_size=batch_size, shuffle=True
    )

    # model_fire = load_model('Output/Models/model_fire_resnet_weighted_40_no_metric_simple')

    # _ = model_fire.evaluate(test_ds, batch_size=batch_size)


    model_file = 'xception_save_at_%d.h5' % 1
    model_fire = load_model(model_file)

    best_model_fire = load_model('xception_save_at_1.h5')
    results_eval = best_model_fire.evaluate(test_ds, batch_size=batch_size)

    for name, value in zip(model_fire.metrics_names, results_eval):
        print(name, ': ', value)
    print()
    print("results:", results_eval)
    cm = np.array([[results_eval[1], results_eval[4]], [results_eval[2], results_eval[3]]])
    cm_plot_labels = ['Fire', 'No Fire']
    plot_confusion_matrix(cm=cm, classes=cm_plot_labels, title='Confusion Matrix')

    # test_fire_ds = tf.keras.preprocessing.image_dataset_from_directory(
    #     "frames/Test/Fire", seed=1337, image_size=image_size, batch_size=batch_size, shuffle=True)
    # test_no_fire_ds = tf.keras.preprocessing.image_dataset_from_directory(
    #     "frames/Test/No_Fire", seed=1337, image_size=image_size, batch_size=batch_size, shuffle=True)
    # fire_eval = model_fire.evaluate(test_fire_ds)
    # no_fire_eval = model_fire.evaluate(test_no_fire_ds)
    # true_fire = len(tf.io.gfile.listdir("frames/Test/Fire"))
    # true_no_fire = len(tf.io.gfile.listdir("frames/Test/No_Fire"))
    # tp = fire_eval[1] * true_fire
    # fp = (1 - fire_eval[1]) * true_fire
    # tn = (1 - no_fire_eval[1]) * true_no_fire
    # fn = no_fire_eval[1] * true_no_fire
    # cm = np.array([[tp, fn], [fp, tn]], dtype=int)
    # plot_confusion_matrix(cm=cm, classes=cm_plot_labels, title='Confusion Matrix')
