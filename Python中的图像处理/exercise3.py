from PIL import Image
from numpy import *
from scipy.ndimage import filters
import matplotlib.pyplot as plt

im = array(Image.open('C:\\Users\\lenovo\\Desktop\\img\\1.jpg').convert('L'), 'f')
# Sobel 导数滤波器
imx = zeros(im.shape)
filters.sobel(im, 1, imx)
imy = zeros(im.shape)
filters.sobel(im, 0, imy)
magnitude = sqrt(imx ** 2 + imy ** 2)

plt.figure("imx")
plt.imshow(imx, cmap='gray')

plt.figure("imy")
plt.imshow(imy, cmap='gray')

plt.figure("magnitude")
plt.imshow(magnitude, cmap='gray')

plt.figure("imximx")
plt.contour(imx, origin='image')
plt.figure("imyimy")
plt.contour(imy, origin='image')
plt.figure("magnitudemagnitude")
plt.contour(magnitude, origin='image')

plt.show()
