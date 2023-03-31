import matplotlib.pyplot as plt
import cv2
from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms
import numpy as np
'''
reference =cv2.imread('D:\dataset\data\ISIC_0024339.jpg')
reference_m = cv2.cvtColor(reference, cv2.COLOR_BGR2RGB)

plt.imshow(reference_m)

import os
os.makedirs('D:\dataset\match_2')

base = "D:\dataset\data"
target = 'D:\dataset\match_2'

a=0

for i in os.listdir('D:\dataset\data'):
    image = cv2.imread(os.path.join(base, i))
    #image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    matched = match_histograms(image, reference_m, channel_axis=2,)
    matched = cv2.cvtColor(matched,cv2.COLOR_BGR2RGB)
    cv2.imwrite(os.path.join(target, i),np.asarray(matched))
    a=a+1
    print(a)
'''
import os
print(len(os.listdir('D:\dataset\match_2')))
print(len(os.listdir('D:\dataset\data')))
  
