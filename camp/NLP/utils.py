import numpy as np
from matplotlib import pyplot as plt

def show_img(filename, size_inch):
    img = plt.imread(filename)
    plt.rcParams['figure.figsize'] = [size_inch, size_inch]
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
