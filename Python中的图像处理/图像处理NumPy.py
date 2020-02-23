from PIL import Image
from numpy import *
import imtools
im = array(Image.open('C:\\Users\\lenovo\\Desktop\\img\\1.jpg').convert('L'))
im2 = 255 - im  # 对图像进行反相处理
im3 = (100.0/255) * im + 100  # 将图像像素值变换到100...200 区间
im4 = 255.0*(im/255.0)**2  # 对图像像素值求平方后得到的图像
print(int(im.min()), int(im.max()))

im = array(Image.open('C:\\Users\\lenovo\\Desktop\\img\\1.jpg').convert('L'))
im2, cdf = imtools.histeq(im)
