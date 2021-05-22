#coding=utf-8
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import re

Name = ['中国国家博物馆', '北京军事博物馆', '故宫博物院', '北京鲁迅博物馆', '中国美术馆', '毛主席纪念堂', '民族文化宫博物馆', '中国地质博物馆',
		'中国古动物馆', '中华航天博物馆', '中国人民抗日战争纪念馆', '中国科学技术馆', '宋庆龄故居', '中国人民革命军事博物馆', '中国航空博物馆',
		'北京天文馆', '首都博物馆', '大钟寺古钟博物馆', '北京艺术博物馆', '北京古代建筑博物馆', '北京石刻艺术博物馆', '徐悲鸿纪念馆',
		'炎黄艺术馆', '明十三陵博物馆', '北京古观象台', '郭沫若纪念馆', '梅兰芳纪念馆', '中国佛教图书文物馆', '中国长城博物馆', '雍和宫藏传佛教艺术博物馆',
		'北京古代钱币博物馆', '北京西周燕都遗址博物馆', '北京辽金城垣博物馆', '北京大葆台西汉墓博物馆', '北京大学赛克勒考古与艺术博物馆', '北京市白塔寺管理处',
		'李大钊烈士陵园', '詹天佑纪念馆', '焦庄户地道战遗址纪念馆', '中央民族大学民族博物馆', '北京航空馆', '北京房山云居寺石经陈列馆', '北京市昌平区博物馆',
		'北京红楼文化艺术博物馆']

def getpage(url,s):
	result=[]
	res=requests.get(url)
	res.encoding='utf-8'
	soup=BeautifulSoup(res.text,'html.parser')
	l=len(soup.select(".tuwenjg li"))
	print(l)
	for i in range(0,l,1):
		ly=soup.select('.tuwenjg .src')[i].text
		bt=soup.select('.tuwenjg .tit a')[i].text
		jj=soup.select('.tuwenjg .bre')[i].text
		sj=soup.select('.tuwenjg .tim')[i].text
		ly=ly[ly.find("：")+1:]
		jj=jj.strip()
		sj=sj[sj.find("：")+1:]
		results=[s,ly,bt,jj,sj]
		result.append(results)
	return result

if __name__ == '__main__':
	u='https://search.cctv.com/search.php?qtext='
	l='&sort=relevance&type=web&vtime=&datepid=1&channel=&page='
	result=[]
	for name in Name:
		for page in range(1,11,1):
			url=u+name+l+str(page)
			print(url)
			result=result+getpage(url,name)
	csv = pd.DataFrame(result)
	csv.to_csv('news.csv')