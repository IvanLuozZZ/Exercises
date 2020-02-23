from PIL import Image
from pylab import *
im = array(Image.open('C:\\Users\\lenovo\\Desktop\\img\\1.jpg'))
imshow(im)
print('Please click 3 points')
x = ginput(3)
print('you clicked:', x)
show()
