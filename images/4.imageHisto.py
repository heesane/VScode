import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('images_chapter_03/ic_ref.jpg',0)
height, width = img.shape
hist = np.zeros((256))

for i in np.arange(height):
    for j in np.arange(width):
        a = img[i][j]
        hist[a] += 1
        
images = [img,hist]
titles = ['Original_img','Histogram']
plt.subplot(1,2,1)
plt.imshow(images[0],cmap ='gray')
plt.title(titles[0])
plt.subplot(1,2,2)
plt.hist(img.ravel(),256,[0,256])
plt.title(titles[1])

plt.subplots_adjust(top = 0.92,bottom = 0.08,left=0.1,right=0.95,hspace = 0.35,wspace=0.35)
plt.show( )