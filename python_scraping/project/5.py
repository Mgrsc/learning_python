from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re#引入正则表达式模块
random.seed(datetime.datetime.now())#用系统当前时间设置随机数生成器的种子
def getLinks(articleUrl):#格式化抓取的页面
	html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))#打开一个url,应用一个格式化，给抓取的url加上wiki的头
	bs = BeautifulSoup(html, 'html.parser')#利用解释器返回赋值给bs
	return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))##先使用find过滤出在div的属性id：...，href先经过正则表达式过滤出href为/wiki/开头，不包含：，匹配前面的规则一次或多次，
links = getLinks('/wiki/Kevin_Bacon')#设置起始页面
while len(links) > 0: #当返回连接长度大于0时一直循环
	newArticle = links[random.randint(0, len(links)-1)].attrs['href']#随意找一个词条链接标签，并抽取href属性
	print(newArticle)#打印整个链接
	links = getLinks(newArticle)#将新连接赋值给links
