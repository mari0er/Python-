#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PIL import Image, ImageDraw, ImageFont


im = Image.open("123.jpg")	#创建图片对象 和代码在同一目录
w,h = im.size	#获取图片的宽和高
font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf',int(h/4))
#创建字体对象，字体大小为高度的1/4   补充一下在deepin系统里找字体的绝对路径是真的坑...

ImageDraw.Draw(im).pieslice([(w/3*2,0),(w,h/3)],0,360,fill = 'red')
# 绘制圆形，第一个参数界定绘制区域，我选择了宽高为原图1/3的右上角区域
# 不难发现坐标系是以左上角为原点，向下y递增，向右x递增

ImageDraw.Draw(im).text((w * 0.76,h * 0.02),'5',font = font,fill = 'white')
# 第一个参数是坐标，第二个参数是文本绘制内容，第三个是字体对象

im.show()	#展示绘制结果
im.save('pci.bak.jpg')