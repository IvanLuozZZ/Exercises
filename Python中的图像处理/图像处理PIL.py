from PIL import Image

# 读取图像
pil_im = Image.open('C:\\Users\\lenovo\\Desktop\\img\\1.jpg')
# 读取图像，并转换成灰度图像
pil_im = Image.open('C:\\Users\\lenovo\\Desktop\\img\\1.jpg').convert('L')
pil_im.show()
# 创建缩略图
pil_im.thumbnail((128,128))
# 裁剪指定区域
box = (100, 100, 400, 400)
region = pil_im.crop(box)
# 旋转并粘贴回去
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region, box)
# 调整尺寸
out = pil_im.resize((128,128))
# 旋转图像
out = pil_im.rotate(45)
out.show()
