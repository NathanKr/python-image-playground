from PIL import Image
import os
from os.path import join 
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

current_dir = os.path.abspath(".")
data_dir = join(current_dir, 'data')
file_name = join(data_dir,"ex3data1.mat") # mnist AndrewNg Coursera
mat_dict = sio.loadmat(file_name)

X = mat_dict["X"]
y = mat_dict["y"]
m = y.size

def plot_image(ax , sample,_X,_y):
    image = _X[sample].reshape(20,20)
    ax.set_title(f'image of X[{sample}] , y[{sample}][0] : {_y[sample][0]} ')
    ax.imshow(image, cmap='gray')


def plot_images(ax ,images_in_row, samples,_X,_y):
    """
        function is working ONLY if len(samples) % images_in_row is zero
    Args:
        ax ([type]): [description]
        images_in_row ([type]): [description]
        samples ([type]): [description]
        _X ([type]): [description]
        _y ([type]): [description]
    """
    images = []
    sample = 0
    image_height = 20
    image_width = 20

    while sample < len(samples):
        images_row = []
        for _ in range(images_in_row):
            images_row.append(_X[sample].reshape(image_height,image_width))
            sample += 1
            if sample == len(samples):
                break
        
        merged_images_horizontal = np.concatenate(images_row,axis=1)  # append horizontaly
        images.append(merged_images_horizontal)

    merged_row_images_vertically = np.concatenate(images,axis=0) # append vertically
    ax.imshow(merged_row_images_vertically, cmap='gray')
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)


fig , ax1 = plt.subplots(1)
# this is working because 50/10 is integer number
images_in_row = 10
plot_images(ax1,images_in_row,np.arange(50),X,y)
fig.suptitle('all images fit into the 10 images per line')
plt.show()

# in case you have 51 images you can split it to two plot_images
fig , (ax1,ax2) = plt.subplots(2)
samples = np.arange(54)
plot_images(ax1,10,samples[:50],X,y)
plot_images(ax2,4,samples[50:54],X,y)
fig.suptitle('50 images fit into the 10 images per line , 4 image fit into 4 images per line')
plt.show()


