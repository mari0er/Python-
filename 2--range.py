#!/usr/bin/ python
# -*- coding:utf-8 -*-
import random

code_list = []
for i in range(10):
	code_list.append(str(i))	#打印数字0-9

for i in range(65, 91):
	code_list.append(chr(i))	#打印大写字母A-Z

for i in range(97, 123):
	code_list.append(chr(i))	#打印小写字母a-z

myslist = random.sample(code_list, 8)	#数字8规定字符串的长度
last_code = ''.join(myslist)
print (last_code)


#下面这个不是更简单吗？干嘛写那么多
'''
my_list = 'qwertyuiopasdfghjklzxcvbnm1234567890+_)(*&^%$#@!QAZWSXEDCRFVTGBYHNUJMIKLOPB'
for i in range(20):
	code = random.sample(my_list, 8)
	print (''.join(code))
'''
