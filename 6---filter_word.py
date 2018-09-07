#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def get_filters():
	filters = []
	with open ('filtered_words.txt','r') as f:
		for line in f.readlines():
			filters.append(line.strip()) #去掉每行后面的回车
	return filters

def main_0011():		#单纯判断有无敏感词语
	filters = get_filters()
	you_put = input("plz input: ")
	if you_put in filters:
		print ("freadm")
	else:
		print ("Human Rights")

def main_0012():		#将敏感词语变成***
	filters = get_filters()
	you_put = input("plz input: ")
	for filter_word in filters:
		new_str = ''
		if filter_word in you_put:
			if len(re.findall(u"[\u4e00-\u9fa5]+",filter_word.decode("utf-8"))) > 0:  #正则判断敏感词是不是中文
				len_new_str = (len(filter_word)) / 3	 #统计中文敏感词语的长度，用相同长度*代替
			else:
				len_new_str = 1		#不是中文就是英文单词，单词就用一个*替换

			for i in range(len_new_str):
				new_str += "*"
			you_put = str(you_put).replace(filter_word,new_str)
	print (you_put)

if __name__ == '__main__':
	main_0011()
	main_0012()
