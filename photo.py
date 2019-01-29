from PIL import Image
i = Image.open('E:\SAM_2871.JPG')
print i.format, i.size, i.mode
i.thumbnail((100,100))
i.save('beihai.png','PNG')
