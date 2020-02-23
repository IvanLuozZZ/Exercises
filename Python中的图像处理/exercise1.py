from PIL import Image
from numpy import *
from scipy.ndimage import filters
import matplotlib.pyplot as plt

""" 
    显示了随着 σ 的增加，一幅图像被模糊的程度。σ 越大，处理后的图像细节 丢失越多 
    模糊灰度图 
"""
im = array(Image.open('C:\\Users\\lenovo\\Desktop\\img\\1.jpg'))
# im2 = filters.gaussian_filter(im,5)

imc = array(Image.open('C:\\Users\\lenovo\\Desktop\\img\\1.jpg').convert('L'))
imc2 = filters.gaussian_filter(imc, 5)

# 反锐化
# im2a = im - im2
imc2a = imc - imc2

im2 = zeros(im.shape)
""" 
    如果打算模糊一幅彩色图像，只需简单地对每一个颜色通道进行高斯 模糊： 
    模糊彩色图 
"""
for i in range(3):
    im2[:, :, i] = filters.gaussian_filter(im[:, :, i], 5)
# im2 = uint8(im2) #im2 = array(im2,'uint8')
im2a = im - im2

plt.figure("broiler")

plt.subplot(411)
plt.imshow(im2)  # 显示的是黄绿图 或者说是热量图 如果需要显示灰度图 需添加参数,cmap = 'gray'

plt.subplot(412)
plt.imshow(im2a)

plt.subplot(413)
plt.imshow(imc2, cmap='gray')  # 显示的是黄绿图 或者说是热量图 如果需要显示灰度图 需添加参数,cmap = 'gray'

plt.subplot(414)
plt.imshow(imc2a, cmap='gray')

plt.show()
