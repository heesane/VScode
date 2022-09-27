import numpy as np
import matplotlib.pyplot as plt
import math

def cumulative_histogram(hist):
    cum_hist = hist.copy()
    for i in np.arange(1,256):
        cum_hist[i]=cum_hist[i-1]+cum_hist[i]
    return cum_hist

def histogram(img):
    height,width = img.shape
    hist = np.zeros((256))
    for i in np.arange(height):
        for j in np.arange(width):
            a = img[i][j]
            hist[a] += 1
    return hist

img = plt.imread('images_chapter_03/Fig6.38(c).jpg',0)
height, width = img.shape
pixels = width * height

hist = histogram(img)
cum_hist =cumulative_histogram(hist)
img_eq = np.zeros(img.shape,img.dtype)
for i in np.arange(height):
    for j in np.arange(width):
        a = img[i][j]
        img_eq[i][j]=math.floor(cum_hist[a]*255.0/pixels)
images = [img,img_eq]
titles = ['Original_img','histogram_equlization']

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],cmap ='gray')
    plt.title(titles[i])
plt.show()