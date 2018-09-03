#!/usr/bin/env python
# -*- coding: utf-8 -*-


from uuid import uuid1
from PIL import Image ,ImageDraw,ImageFont,ImageFilter
import random

def ran_char():
	'''
	随机产生一个字符串
	'''
	lists = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	random_char = random.sample(lists,1)
	return (''.join(random_char))

def ran_color1():
	'''
	随机颜色1
	'''
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def ran_color2():
	'''
	随机颜色2
	'''
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

def create_code():
	'''
	生成图片验证码
	'''
	width = 120
	height = 50    #定义图片的大小
	image = Image.new('RGB',(width,height),(192,192,192))
	#image.show()
	font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf',36)     #定义字体类型和大小，不同系统路径可能不同
	draw = ImageDraw.Draw(image)

	#随机颜色填充每个像素点
	for x in range(0,width,2):
		for y in range(0,height,1):
			draw.point((x,y),fill = ran_color1())

	#填入四个随机字符作为验证码
	_str = ""
	for i in range(4):
		my_str = ran_char()
		_str = "{}{}".format(_str,my_str)	#_str为最后生成的字符串
		#print (_str)
		h = 10      #规定字符距离图片上边界的距离
		w = width/4 * i + 5     #规定每个字符间的距离
		draw.text((w,h),my_str,font = font ,fill = ran_color2())
	image.filter(ImageFilter.BLUR)	#模糊处理
	name = '{}.jpg'.format(uuid1())	#利用uuid生成的唯一字符串作为保存的文件名
	#image.show()
	image.save(name)


if __name__ == '__main__':
	create_code()