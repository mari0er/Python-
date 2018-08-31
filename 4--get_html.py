#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

#自定义浏览器头
headers = {
	'Host': "www.mari0er.club",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"
}
requests = requests.Session()
my_url = "https://www.mari0er.club"

def get_doc_url():
	result = {}
	req = requests.get(my_url,headers = headers, verify = False)
	soup = BeautifulSoup(req.text,"lxml")	#获取链接的网页源码
	#print (soup)
	tmps = soup.find_all("div",class_ = "article-title")      #找到所有class等于article-title的div标签
	for tmp in tmps:
		title = (tmp.get_text()).strip()
		url = (tmp.find_all('a')[0])['href']	#这里记录一下，heaf链接在div标签下的a标签中，所以有点麻烦 不能直接url = tmp.get('href')
		result[title] = url 	#将标题和url链接存在字典中
	return result
	#print (result)


def down_html(url_dict):
	if len(url_dict) < 1:
		return

	for name ,url in url_dict.items():
		req = requests.get(url,headers = headers, verify = False)	#打开字典中的每一个链接，保存其html代码
		with open (name + ".html","wb") as file:
			for chunk in req.iter_content(1024):
				file.write(chunk)

if __name__ == '__main__':
	a = get_doc_url()
	down_html(a)
