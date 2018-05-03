
# 改变图片大小 143 * 143

from PIL import Image
import os
### path， 照片的路径
### factor，缩放的比例
def resize(path, factor=0.9):
    img  = Image.open(path)
    # out = img.resize(tuple(map(lambda x: int(x * factor), img.size)))
    out = img.resize((143, 143), Image.ANTIALIAS)
    # 保存文件，直接将原来的文件替换掉（有风险，建议备份源文件）
    with open(path, 'w') as f:
        out.save(f)
    return path


base_path = 'D:/imgs/'
# 遍历这个文件夹，找到所有jpg文件，然后拿到文件路径（绝对路径）
files = [os.path.abspath(base_path + item) for item in os.listdir(base_path)
  if len(item.split('.')) == 2 and item.split('.')[1] == 'jpg']

# 执行
list(map(resize, files))
