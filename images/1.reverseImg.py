import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('images_chapter_03/Fig3.15(a)1top.jpg',0)
height = img.shape[0]
width = img.shape[1]
max_intensity = 255
s_img = np.zeros(img.shape,img.dtype)

for i in np.arange(height):
    for j in np.arange(width):
        s_img[i][j] = max_intensity - img[i][j]
        
images = [img,s_img]
titles = ['Original image','Reverse iamg']

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],cmap = 'gray')
    plt.title(titles[i])
plt.show()