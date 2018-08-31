#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import Counter    #导入计数模块


def cal(filename = 'test.txt'):
	with open (filename,'r') as f:
		data = f.read()
	data = data.lower()
	datalist = re.split(r'[\s\n]+',data)    #利用正则根据空格和换行进行分割
	return Counter(datalist).most_common()    #利用Counter计数

if __name__ == '__main__':
	dic = cal()
	#print (dic)
	for i in range(len(dic)):
		print ('%15s  ---->    %s' % (dic[i][0],dic[i][1]))


