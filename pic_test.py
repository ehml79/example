from PIL import Image

im = Image.open('D:/imgs/0.jpg')
im_head = Image.open('D:/head.jpg')
#设置要拷贝的区域
box = (0, 0, 100, 100)

# 将im表示的图片对象拷贝到region中，大小为(400*400)像素。
# 这个region可以用来后续的操作(region其实就是一个Image对象)，
# box变量是一个四元组(左，上，右，下)。
region  = im.crop(box)

# 从字面上就可以看出，先把region中的Image反转180度，然后再放回到region中。
region = region.transpose(Image.ROTATE_90)
#粘贴box大小的region到原先的图片对象中。
im.paste(region, box)
# im.save('D:/imgs2/0.jpg')
im.show()


