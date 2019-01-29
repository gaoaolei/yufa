'''
2.7---PIL    3.6---pillow
# pip install PIL             2.7
# pip install pillow        3.6
# pip install PIL -i https://pypi.douban.com/simple/
# pip install SomePackage==8.9.5    #指定版本
# pip install 'SomePackage>=8.9.5'  #最小版本
# pip install PIL -U                #更新安装

'''

from PIL import Image
i = Image.open('pil.jpg')
print(i.format, i.size, i.mode)
i.thumbnail((600, 600))
i.save('pil_new.png', 'JPEG')
