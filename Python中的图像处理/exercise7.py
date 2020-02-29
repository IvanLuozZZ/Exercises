from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import measurements, morphology, label

im=array(Image.open('C:\\Users\\lenovo\\Desktop\\img\\1.jpg').convert('L'))
im=1*(im < 128)

#载入图像，然后使用阈值化操作，以保证处理的图像为二值图像
im_open = morphology.binary_opening(im, ones((5, 5)), iterations=2)

labels_open, nbr_objects_open = measurements.label(im_open)

# 求出每个物体中心点坐标
a=measurements.center_of_mass(im_open, labels_open, [i+1 for i in range(nbr_objects_open)])

figure()
gray()
imshow(im_open)

# 在图像中把中心点绘制出来
plot([p[1] for p in a], [p[0] for p in a], 'r*')

show()
