import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('images_chapter_03/Fig3.09(a).jpg',0)
height, width = img.shape
gamma_table =[1.0,3.0,4.0,5.0]
titles = ["Oriingal","Gamma = 3.0","gamma = 4.0","gamma = 5.0"]

for i in range(4):
    gamma = gamma_table[i]
    s_img = np.power(img,gamma)
    s_img /= np.power(250.0,gamma-1)
    plt.subplot(2,2,i+1)
    plt.imshow(s_img,cmap='gray')
    plt.title(titles[i])
    
plt.subplots_adjust(top = 0.92,bottom = 0.08,left=0.1,right=0.95,hspace = 0.35,wspace=0.35)
plt.show()