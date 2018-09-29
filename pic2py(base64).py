# -*- coding :UTF-8 -*-

import base64
 
def pic2py(picture_name):
    open_pic = open("%s" % picture_name, 'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()
    
    # 注意这边b64str一定要加上.decode()
    write_data = 'img = "%s"' % b64str.decode()
    f = open('%s.py' % picture_name.replace('.', '_'), 'w+')
    f.write(write_data)
    f.close()
 
if __name__ == '__main__':
    name = input("你想转化的图片的完整文件名：")
    pic2py(name)

#使用方式如下

'''
from in_ico import img
...
tmp = open('in.ico', 'wb')
tmp.write(base64.b64decode(img))
tmp.close()

#使用图片

os.remove('in.ico')
'''
