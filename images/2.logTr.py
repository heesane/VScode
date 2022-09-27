import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('images_chapter_03/Fig3.05(a).jpg',0)
height = img.shape[0]
width = img.shape[1]

# =============================================================================
# s_img = np.log10(1.0+img)
# s_img = 255* s_img /np.log10(256.0)
# images = [img,s_img]
# titles = ["Original_img","LogTransform_img"]
# 
# for i in range(2):
#     plt.subplot(1,2,i+1)
#     plt.imshow(images[i],cmap='gray')
#     plt.title(titles[i])
# plt.show()
# 
# =============================================================================
