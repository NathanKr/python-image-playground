from PIL import Image
import numpy as np


def plot_image(ax , sample,_X,_y):
    image = _X[sample].reshape(20,20)
    ax.set_title(f'image of X[{sample}] , y[{sample}][0] : {_y[sample][0]} ')
    ax.imshow(image, cmap='gray')


def plot_images(ax ,images_in_row,image_height, image_width,samples,_X,_y):
    """
        function is working ONLY if len(samples) % images_in_row is zero
    
    """
    images = []
    sample = 0

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

