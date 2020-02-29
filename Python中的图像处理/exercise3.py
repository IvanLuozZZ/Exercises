from PIL import Image
from numpy import *
from scipy.ndimage import filters
import matplotlib.pyplot as plt

"""  
    显示了随着 σ 的增加，一幅图像被模糊的程度。σ 越大，处理后的图像细节 丢失越多  
    模糊灰度图  
"""

imc = array(Image.open('C:\\Users\\lenovo\\Desktop\\img\\1.jpg').convert('L'))  # 读取灰色图
imc2 = filters.gaussian_filter(imc, 5)  # 灰色图高斯滤波
imc2a = imc - imc2  # 灰度图反锐化
imc2as = imc / imc2

im = array(Image.open('C:\\Users\\lenovo\\Desktop\\img\\1.jpg'))  # 读取彩色图
im2 = zeros(im.shape)
"""  
    如果打算模糊一幅彩色图像，只需简单地对每一个颜色通道进行高斯 模糊：  
    模糊彩色图  
"""
for i in range(3):
    im2[:, :, i] = filters.gaussian_filter(im[:, :, i], 5)  # 彩色图高斯滤波 三通道
im2a = im - im2  # 彩色图反锐化
im2as = im / im2

plt.figure("broiler")

plt.subplot(611)
plt.imshow(im2)  # 彩色高斯滤波图

plt.subplot(612)
plt.imshow(im2a)  # 彩色反锐化图

plt.subplot(613)
plt.imshow(im2as)  # 彩色商图像

plt.subplot(614)
plt.imshow(imc2, cmap='gray')  # 灰色高斯滤波图

plt.subplot(615)
plt.imshow(imc2a, cmap='gray')  # 灰色反锐化图

plt.subplot(616)
plt.imshow(imc2as)  # 灰色商图像

plt.show()
