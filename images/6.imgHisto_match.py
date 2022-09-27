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

def hist_match(img,img_ref):
    height,width = img.shape
    pixels = width*height
    
    height_ref,width_ref = img_ref.shape
    pixels_ref = width_ref *height_ref
    
    hist = histogram(img)
    hist_ref = histogram(img_ref)
    cum_hist = cumulative_histogram(hist)
    cum_hist_ref = cumulative_histogram(hist_ref)
    
    prob_cum_hist = cum_hist/pixels
    prob_cum_hist_ref = cum_hist_ref / pixels_ref
    
    new_hist = np.zeros(256)
    
    for i in range(256):
        hist_min = 1000;
        for j in range(256):
            hist_diff = np.abs(prob_cum_hist[i] - prob_cum_hist_ref[j])
            if hist_diff < hist_min:
                hist_min = hist_diff
                hist_index =j
        new_hist[i] = hist_index
    
    s_img = np.zeros(img.shape,img.dtype)
    for i in np.arange(height):
        for j in np.arange(width):
            a = img[i][j]
            s_img[i][j] = new_hist[a]
    return s_img

img = plt.imread('images_chapter_03/saturn_noise.jpg',0)
img_ref = plt.imread('images_chapter_03/saturn_spec.jpg',0)

img_match = hist_match(img,img_ref)
images = [img,img_ref,img_match]
titles = ['Original_img','img_ref','img_match']

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],cmap='gray')
    plt.title(titles[i])
    
plt.subplots_adjust(top = 0.92,bottom = 0.08,left=0.1,right=0.95,hspace = 0.35,wspace=0.35)
plt.show()