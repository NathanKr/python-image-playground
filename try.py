import os
from os.path import join 
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from utils import plot_images

current_dir = os.path.abspath(".")
data_dir = join(current_dir, 'data')
file_name = join(data_dir,"ex3data1.mat") # mnist AndrewNg Coursera
mat_dict = sio.loadmat(file_name)

X = mat_dict["X"]
y = mat_dict["y"]
m = y.size

fig , ax1 = plt.subplots(1)
# this is working because 50/10 is integer number
images_in_row = 10
image_height = 20
image_width = 20
plot_images(ax1,images_in_row,image_height, image_width,np.arange(50),X,y)
fig.suptitle('all images fit into the 10 images per line')
plt.show()

# in case you have 51 images you can split it to two plot_images
fig , (ax1,ax2) = plt.subplots(2)
samples = np.arange(54)
plot_images(ax1,10,image_height, image_width,samples[:50],X,y)
plot_images(ax2,4,image_height, image_width,samples[50:54],X,y)
fig.suptitle('50 images fit into the 10 images per line , 4 image fit into 4 images per line')
plt.show()


