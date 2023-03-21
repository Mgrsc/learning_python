# python_scraping

## What's web scraping

web scraping的程序叫做web crawler（网络爬虫） or bot（网络机器人），理论上，网页抓取是一种通过多种手段收集网络数据的方式，不光是通过与API 交互（或 者直接与浏览器交互）的方式。最常用的方法是写一个自动化程序向网络服务器请求数据 （通常是用HTML 表单或其他网页文件），然后对数据进行解析，提取需要的信息。

### The benefits of web crawlers



- 处理能力卓越：可以一次看上千上万个网页
- 做网页不能做的事：抓取大量网站，绘制出飞机价格随时间的变化，告诉我购买机票的最佳时机。
- 毫无阻碍的获取数据无需API





## 库

### urllib --- URL 处理模块

urllib 是一个收集了多个涉及 URL 的模块的包： 

#### [urllib.request](https://docs.python.org/zh-cn/3/library/urllib.request.html#module-urllib.request) 

打开和读取 URL 

函数：

##### .urlopen

urlopen返回的是HTTPResposne类型的对象。得到这个对象之后，我们把它赋值为变量，然后就可以调用这些方法【read()、readinto()、getheader(name)、getheaders()、fileno()等方法，以及msg、version、status、reason、debuglevel、closed】和属性，得到返回结果的一系列信息了。

例如，调用read()方法可以得到返回的网页内容，调用status属性可以得到返回结果的状态码，如200代表请求成功，404代表网页未找到等。

**urllib.request.urlopen(*url*, *data=None*, [*timeout*, ]***, *cafile=None*, *capath=None*, *cadefault=False*, *context=None*)**

打开统一资源定位符 *url*，可以是一个字符串或一个 [`Request`](https://docs.python.org/zh-cn/3/library/urllib.request.html#urllib.request.Request) 对象。

*data* 必须是一个对象，用于给出要发送到服务器的附加数据，若不需要发送数据则为 `None`。详情请参阅 [`Request`](https://docs.python.org/zh-cn/3/library/urllib.request.html#urllib.request.Request) 。

urllib.request 模块采用 HTTP/1.1 协议，并且在其 HTTP 请求中包含 `Connection:close` 头部信息。

*timeout* 为可选参数，用于指定阻塞操作（如连接尝试）的超时时间，单位为秒。如未指定，将使用全局默认超时参数）。本参数实际仅对 HTTP、HTTPS 和 FTP 连接有效。

如果给定了 *context* 参数，则必须是一个 [`ssl.SSLContext`](https://docs.python.org/zh-cn/3/library/ssl.html#ssl.SSLContext) 实例，用于描述各种 SSL 参数。更多详情请参阅 [`HTTPSConnection`](https://docs.python.org/zh-cn/3/library/http.client.html#http.client.HTTPSConnection) 。

*cafile* 和 *capath* 为可选参数，用于为 HTTPS 请求指定一组受信 CA 证书。*cafile* 应指向包含CA 证书的单个文件， *capath* 则应指向哈希证书文件的目录。





#### [urllib.error](https://docs.python.org/zh-cn/3/library/urllib.error.html#module-urllib.error) 

包含 urllib.request 抛出的异常 

函数：

##### .URLError

服务器不存在

如果服务器不存在（就是说链接http://www.pythonscraping.com 打不开，或者是URL 链接
写错了），urlopen 会抛出一个URLError 异常。这就意味着获取不到服务器，并且由于远程
服务器负责返回HTTP 状态代码，所以不能抛出HTTPError 异常，而且还应该捕获到更严
重的URLError 异常

```python
可以这样检测
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
	html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e:
	print(e)
except URLError as e:
	print('The server could not be found!')
else:
	print('It Worked!')
```



##### .HTTPError

服务器上不存在或者获取页面出现错误或返回http错误，可能是404 500等，urlopen都会抛出HTTPError异常

```python
遇到这种异常可以
from urllib.request import urlopen
from urllib.error import HTTPError
try:
	html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
	print(e)
# 返回空值，中断程序，或者执行另一个方案
else:
# 程序继续。注意：如果你已经在上面异常捕捉那一段代码里返回或中断（break），
# 那么就不需要使用else语句了，这段代码也不会执行
```



##### AttributeError

即使从服务器成功获取网页，如果网页上的内容并非完全是我们期望的那样，仍然
可能会出现异常。每当你调用BeautifulSoup 对象里的一个标签时，增加一个检查条件以
保证标签确实存在是很聪明的做法。如果你想要**调用的标签不存在**，BeautifulSoup 就会返
回None 对象。不过，如果**再调用这个None 对象下面的子标签**，就会发生AttributeError
错误。

```
(即调用之后不检查再次将调用子标签就会抛出AttributeError)
print(bs.nonExistentTag)
print(bs.nonExistentTag.someTag)
抛出异常AttributeError: 'NoneType' object has no attribute 'someTag'
```

避免可以使用以下代码

```python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bs = BeautifulSoup(html.read(), 'html.parser')##.read获取html内容，bs读取html并解释
		title = bs.body.h1
	except AttributeError as e:
		return None
		return title
title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
	print('Title could not be found')
else:
	print(title)
```



#### [urllib.parse](https://docs.python.org/zh-cn/3/library/urllib.parse.html#module-urllib.parse) 

用于解析 URL 

```
urlparse() 函数可以将 URL 解析成 ParseResult 对象。对象中包含了六个元素，分别为：

协议（scheme） 
域名（netloc） 
路径（path） 
路径参数（params） 
查询参数（query） 
片段（fragment）
```





#### [urllib.robotparser](https://docs.python.org/zh-cn/3/library/urllib.robotparser.html#module-urllib.robotparser) 

用于解析 robots.txt 文件









### Beautifulsoup

Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.Beautiful Soup会帮你节省数小时甚至数天的工作时间.

`BeautifulSoup(html.read(该对象所基于的html文本), 'html.parser(解析器)')`

可以解析对象，然后并按照标准缩进输出，常用的解析器有`html.parser`,`lxml`,`html5lib`；首先传入对象被转化为unicode然后使用合适的解释器来解释这段文档

```python
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
#BeautifulSoup 还可以使用urlopen 直接返回的文件对象，而不需要先调用.read() 函数
bs = BeautifulSoup(html, 'html.parser')
```

![image-20221107152447961](C:\Users\Mgrsc\Desktop\study\it\programme\pyhton\python_scraping\assets\image-20221107152447961.png)


选中特定结构化数据的方法：

```python
soup.title
# <title>The Dormouse's story</title>

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']
# u'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
```





#### 对象种类

*Python*是一种面向*对象*的编程语言。在*Python*中,所有事物都被视为*对象*,包括变量,函数,列表,元组,字典,集合等。每个*对象*都属于其类。例如- 整数变量属于整数类。所以对象种类就是Beautifulsoup类的对象的种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: `Tag` , `NavigableString` , `BeautifulSoup` , `Comment` .

##### Tag

BeautifulSoup 对象通过find 和find_all，或者直接调用子标签获取的一列对象或单个对象，就像：

```python
bs.div.h1
```

`Tag` 对象与XML或HTML原生文档中的tag相同:

```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
type(tag)
# <class 'bs4.element.Tag'>
```

###### Name

每个tag都有自己的名字通过`.name`获取

```python
tag.name
# u'b'
```

如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档:

```python
tag.name = "blockquote"
tag
# <blockquote class="boldest">Extremely bold</blockquote>
```

###### Attributes

一个tag可能有很多个属性. tag `<b class="boldest">` 有一个 “class” 的属性,值为 “boldest” . tag的属性的操作方法与字典相同:

```python
tag['class']
# u'boldest'
```

也可以直接”点”取属性, 比如: `.attrs` :

```python
tag.attrs
# {u'class': u'boldest'}
```

tag的属性可以被添加,删除或修改. 再说一次, tag的属性操作方法与字典一样

```python
tag['class'] = 'verybold'
tag['id'] = 1
tag
# <blockquote class="verybold" id="1">Extremely bold</blockquote>

del tag['class']
del tag['id']
tag
# <blockquote>Extremely bold</blockquote>

tag['class']
# KeyError: 'class'
print(tag.get('class'))
# None
```

###### 多值属性

HTML 4定义了一系列可以包含多个值的属性.在HTML5中移除了一些,却增加更多.最常见的多值的属性是 class (一个tag可以有多个CSS的class). 还有一些属性 `rel` , `rev` , `accept-charset` , `headers` , `accesskey` . 在Beautiful Soup中多值属性的返回类型是list:

```python
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.p['class']
# ["body", "strikeout"]

css_soup = BeautifulSoup('<p class="body"></p>')
css_soup.p['class']
# ["body"]
```

如果某个属性看起来好像有多个值,但在任何版本的HTML定义中都没有被定义为多值属性,那么Beautiful Soup会将这个属性作为字符串返回

```python
id_soup = BeautifulSoup('<p id="my id"></p>')
id_soup.p['id']
# 'my id'
```

将tag转换成字符串时,多值属性会合并为一个值

```python
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
rel_soup.a['rel']
# ['index']
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>
```

如果转换的文档是XML格式,那么tag中不包含多值属性

```python
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
xml_soup.p['class']
# u'body strikeout'
```

###### 可遍历的字符串

字符串常被包含在tag内.Beautiful Soup用 `NavigableString` 类来处理tag中的字符串:

```python
tag.string
# u'Extremely bold'
type(tag.string)
# <class 'bs4.element.NavigableString'>
```

一个 `NavigableString` 字符串与Python中的Unicode字符串相同,并且还支持包含在 [遍历文档树](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id19) 和 [搜索文档树](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id28) 中的一些特性. **通过 `unicode()` 方法可以直接将 `NavigableString` 对象转换成Unicode字符串**:

```python
unicode_string = unicode(tag.string)
unicode_string
# u'Extremely bold'
type(unicode_string)
# <type 'unicode'>
```

tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用 [replace_with()](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#replace-with) 方法:

```python
tag.string.replace_with("No longer bold")
tag
# <blockquote>No longer bold</blockquote>
```

`NavigableString` 对象支持 [遍历文档树](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id19) 和 [搜索文档树](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id28) 中定义的大部分属性, 并非全部.尤其是,一个字符串不能包含其它内容(tag能够包含字符串或是其它tag),字符串不支持 `.contents` 或 `.string` 属性或 `find()` 方法.

如果想在Beautiful Soup之外使用 `NavigableString` 对象,需要调用 `unicode()` 方法,将该对象转换成普通的Unicode字符串,否则就算Beautiful Soup已方法已经执行结束,该对象的输出也会带有对象的引用地址.这样会浪费内存.







#### BeautifulSoup

##### find()

find(tag, attributes, recursive, text, keywords)

标签参数tag 可以**传递一个标签的名称或多个标签名称组成的Python 列表做标签参数**。例如，下面的代码将返回一个包含HTML 文档中所有标题标签
的列表：

```python
.find_all(['h1','h2','h3','h4','h5','h6'])
```

属性参数attributes 用一个Python 字典**封装一个标签的若干属性和对应的属性值**。例如，下面这个函数会返回HTML 文档里红色与绿色两种颜色的span 标签：

```python
.find_all('span', {'class':{'green', 'red'}})
```

递归参数recursive 是一个**布尔变量**。你想抓取HTML 文档标签结构里多少层的信息？**如果recursive 设置为True，find_all 就会根据你的要求去查找标签参数的所有子标签，以及子标签的子标签**。**如果recursive 设置为False，find_all 就只查找文档的一级标签。**find_all 默认是支持递归查找的（recursive 默认值是True）；一般情况下这个参数不需要设置，除非你真正了解自己需要哪些信息，而且抓取速度非常重要，那时你可以设置递
归参数。

文本参数text 有点不同，它是**用标签的文本内容去匹配**，而不是用标签的属性。假如我们想查找前面网页中包含“the prince”内容的标签数量，可以把之前的find_all 方法换成下面的代码：

```python
nameList = bs.find_all(text='the prince')
print(len(nameList))
```



还有一个关键词参数keyword，**可以让你选择那些具有指定属性的标签**。例如：

```python
title = bs.find_all(id='title', class_='text')
```

上述代码返回第一个在class_ 属性中包含单词text 并且在id 属性中包含title 的标签。需要注意的是，通常情况下，页面中每个id 的属性值只能被使用一次。因此在实际情况中，上面的代码可能并不实用，而以下代码可以达到同样的效果：

```python
title = bs.find(id='title')
```



##### find_all()

find_all(tag, attributes, recursive, text, limit, keywords)

范围限制参数limit 显然只用于find_all 方法。find 其实等价于limit 等于1 时的find_all。**如果你想获取网页中的前x 项结果**，就可以设置它。但是要注意，设置这个参数之后，获得的前几项结果是**按照网页上的顺序排序**的，未必是你想要的那前几项。



##### .get_text()

get_text() 会清除你正在处理的HTML 文档中的所有标签，然后返回一个
只包含文字的Unicode 字符串。假如你正在处理一个包含许多超链接、段落
和其他标签的大段文本，那么.get_text() 会把这些超链接、段落和标签都
清除掉，只剩下一串不带标签的文字。
用BeautifulSoup 对象查找你想要的信息，比直接在HTML 文本里查找信息
要简单得多。通常在你准备打印、存储和操作最终数据时，应该最后才使
用.get_text()。一般情况下，你应该尽可能地保留HTML 文档的标签结构。









##### NavigableString

用来表示标签里的文字，而不是标签本身（有些函数可以操作和生成NavigableString对象，而不是标签对象）。



##### Comment

用来查找HTML 文档的注释标签，<!-- 像这样 -->。



## 抓取和处理

### 异常的处理

防止错误导致运行的爬虫错误

try except 语句的执行流程如下：

1. 首先执行 try 中的代码块，如果执行过程中出现异常，系统会自动生成一个异常类型，并将该异常提交给 Python 解释器，此过程称为捕获异常。
2. 当 Python 解释器收到异常对象时，会寻找能处理该异常对象的 except 块，如果找到合适的 except 块，则把该异常对象交给该 except 块处理，这个过程被称为处理异常。如果 Python 解释器找不到处理异常的 except 块，则程序运行终止，Python 解释器也将退出。
3. 当没有发生异常时候则else语句将执行

#### HTTPError

- 网页不存在于服务器上（404 page not found \   500 internal server error）

对于这类urlopen函数会抛出**HTTPError**一场，我们常用 

```python
from urlib.request import urlopen
from urllib.error import HTTPError

try:
    html = urlopen('http://www/baidu/com')
    #尝试打开如果无法打开则执行else
except HTTPError as e:
    print(e)
 #返回空值，中断程序或者执行其他方案
else:
    #程序继续，如果上面try捕捉到到代码执行break则不会执行该代码
```

![image-20230202113858184](C:\Users\Mgrsc\Desktop\study\it\programme\pyhton\python_scraping\assets\image-20230202113858184.png)

#### URLError

- 服务器不存在

对于服务器不存在这类，就是连接打不开或者url写错了，urlopen就会抛出一个**URLError**异常，意味着获取不到服务器，并且由远程服务器负责返回http状态码，所以无法抛出httperror异常，而且还应该捕获到更严重的urlerror异常，可以增加一些检查代码

![image-20230202114757284](C:\Users\Mgrsc\Desktop\study\it\programme\pyhton\python_scraping\assets\image-20230202114757284.png)

```python
from urlib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://www/baidu/com')
    #尝试打开如果无法打开则执行else
except HTTPError as e:
    print(e)
except URLError as e:
    print(' the server could not be found!')
 #返回空值，中断程序或者执行其他方案
else:
    print('it workd')
    #程序继续，如果上面try捕捉到到代码执行break则不会执行该代码
```





#### AttributeError

从服务器捕获网页成功之后，在调用BeautifulSoup里面一个标签的时候仍会出错，如果调用的标签不存在则会返回none对象，不过如果在调用这个none对象下面的子标签就会发生AttributeError错误

```python
print(bs.asdweqd)  #返回none
print(bs.asdweqd.sadwqd)  #返回AttributeError异常

#对这两种异常进行检查
try:
	badContent = bs.asdweqd.sadwqd
except AttributeError as e:
	print('tag was not found')
else:
	if bad Content == None:
		print('tag was not found')
	else:
		print(badContent)
```









综合一下

```python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
 
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), "html.parser")
        #还检查了URLError，服务器不存在则html为none，则html.read抛出异常AttributeError
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title
 
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found!")
else:
    print(title)
```







### BeautifulSoup抓取和处理

```python
抓取一个红绿文字的页面
from urllib.request import urlopen
from bs4 import BeautifulSoup 
#抓取整个网页
html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
#结构化html创建bs对象
nameList = bs.findAll('span', {'class':'green'})
#使用findAll找到所有span标签里class为green的提取出来
#使用get_text提取出字符串
for name in nameList:
	print(name.get_text())
```

.get_text()会清除所有html标签、段落、超链接然后返回文本



#### BS的find使用方法

见库bs里



### 导航树

通过标签在文档中的位置来查找标签

```python
bs.tag.subTag.anotherSubTag
#bs下的tag下的subtag下的anothersubtag
```

html页面可以映射为一棵树

![image-20221108110325073](C:\Users\Mgrsc\Desktop\study\it\programme\pyhton\python_scraping\assets\image-20221108110325073.png)

#### 1. 处理子标签和其他后代标签

子标签children,后代标签descendants

和许多其他库一样，在BeautifulSoup 库里，孩子（child）和后代（descendant）有显著的不同：和人类的家谱一样，**子标签就是父标签的下一级**，而**后代标签是指父标签下面所有级别的标签**。例如，tr 标签是table 标签的子标签，而tr、th、td、img 和span 标签都是table 标签的后代标签（我们的示例页面中就是如此）。**所有的子标签都是后代标签，但不是所有的后代标签都是子标签。**

一般情况下，**BeautifulSoup 函数总是处理当前标签的后代标签**。例如，bs.body.h1 选择了body 标签后代里的第一个h1 标签，不会去找body 外面的标签。类似地，bs.div.find_all("img") 会找出文档中的第一个div 标签，然后获取这个div 后代里所有img 标签的列表。

**如果你只想找出子标签，可以用.children 标签：**

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
for child in bs.find('table',{'id':'giftList'}).children:
	print(child)
    #这段代码会打印giftList 表格中所有产品的数据行，包括最开始的列名行。如果你用descendants() [后代]函数而不是children()[子标] 函数，那么就会打印出二十几个标签，包括img 标签、span 标签，以及每个td 标签。掌握子标签与后代标签的差别十分重要！
```



#### 2. 处理兄弟标签

之后的兄弟标签next_siblings() ，之前的兄弟标签previous_siblings ()

还有**next_sibling** 和**previous_sibling** 函数， 它们的作用跟next_sibling**s** 和previous_sibling**s** 类似，**只是它们返回的是单个标签，而不是一组标签。**

BeautifulSoup 的next_siblings() 函数使得从表格中收集数据非常简单，尤其是带标题行的表格,**获取除自身之后的兄弟标签**：

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
	print(sibling)
    #这段代码会打印产品表格里所有行的产品，第一行表格标题除外。为什么标题行被跳过了呢？对象不能是自己的兄弟标签。任何时候你获取一个标签的兄弟标签，都不会包含这个标签本身。正如函数名本身揭示的，这个函数只调用后面的兄弟标签。例如，如果我们选择一组标签中位于中间位置的一个标签，然后调用next_siblings() 函数，那么就只会返回在它后面的兄弟标签。因此，选择标题行，然后调用next_siblings，就可以选择表格中除了标题行以外的所有行。
```

如果你很容易找到一组兄弟标签中的最后一个标签， 那么previous_siblings 函数也会很有用。



#### 3. 处理父标签

在抓取网页的时候，查找父标签的需求比查找子标签和兄弟标签要少很多。通常情况下，如果以抓取网页内容为目的来观察HTML 页面，我们都是从最上层标签开始的，然后思考如何定位我们想要的数据块所在的位置。但是，偶尔在特殊情况下你也会用到BeautifulSoup 的**父标签查找函数parent 和parents**。例如：

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('img',
		{'src':'../img/gifts/img1.jpg'})
	.parent.previous_sibling.get_text())  #parent选择父标签，然后在选择前一个兄弟标签
#这段代码会打印../img/gifts/img1.jpg 这个图片所对应商品的价格（这个示例中价格是$15.00）。
#➊ 首先选择图片标签src="../img/gifts/img1.jpg"。
#➋ 选择图片标签的父标签（在示例中是td 标签）。
#➌ 选择td 标签的前一个兄弟标签previous_sibling（在示例中是包含美元价格的td 标签）。
#➍ 选择标签中的文字，“$15.00”。
```



### 正则和lambda

#### 正则表达式（regex)

叫正则表达式是因为它可以识别正则字符串(regular string)，也就是说，它们可以这么定义：“如果你给我的字符串符合规则，就返回它”，或者是“如果字符串不符合规则，我就忽略它”。这在快速浏览大文档，以查找像电话号码和邮箱地址之类的字符串时，是非常方便的。

![image-20221109153049368](C:\Users\Mgrsc\Desktop\study\it\programme\pyhton\python_scraping\assets\image-20221109153049368.png)

正则表达式在实际中的一个经典应用是识别邮箱地址。虽然不同邮箱服务器的邮箱地址的
具体规则不尽相同，但是我们还是可以创建几条通用规则。

![image-20221109153129265](C:\Users\Mgrsc\Desktop\study\it\programme\pyhton\python_scraping\assets\image-20221109153129265.png)

![image-20221109153401162](C:\Users\Mgrsc\Desktop\study\it\programme\pyhton\python_scraping\assets\image-20221109153401162.png)

#### 结合beautifulsoup

在抓取网页的时候，BeautifulSoup 和正则表达式总是配合使用的。其实，大多数支持字符串参数的函数（比如，find(id="aTagIdHere")）也都支持正则表达式。正则表达式可以作为BeautifulSoup 语句的任意一个参数，让你可以灵活地查找目标元素。

例子：抓取网页img，因为现代网站经常有一些用来对齐的白色图片或者logo那么就需要用正则表达式处理。

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re   #引入正则，不引入也行，易读
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img',
{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})  #使用正则
for image in images:
	print(image['src'])
```



#### 获取属性

在抓取网页时你经常不需要查找标签的内容，而是需要查找标签属性。比如标签a 指向的
URL 链接包含在href 属性中，或者img 标签的图片文件包含在src 属性中，这时获取标
签属性就变得非常有用了。
对于一个标签对象，可以用下面的代码获取它的全部属性：
`myTag.attrs`
要注意这行代码**返回的是一个Python 字典对象**，可以轻松获取和操作这些属性。比如要获
取图片的源位置src，可以用下面这行代码：
`myImgTag.attrs['src']`

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'): #遍历bs里的所有a标签并且赋值
    if 'href' in link.attrs:  #如果href标签在赋值的变量里面
        print(link.attrs['href'])  #就打印赋值的变量的所有href标签下的属性

```



### Lambda表达式

Lambda 表达式本质上就是一个函数，可以作为变量传入另一个函数；也就是说，一个函
数不是定义成f(x, y)，而是可以定义成f(g(x), y) 或f(g(x), h(y)) 的形式。

BeautifulSoup 允许我们把特定类型的函数作为参数传入find_all 函数。唯一的限制条件是
这些函数必须把一个标签对象作为参数并且返回布尔类型的结果。BeautifulSoup 用这个
函数来评估它遇到的每个标签对象，最后把评估结果为“真”的标签保留，把其他标签
剔除。

例如，下面的代码就是获取有两个属性的所有标签：
bs.find_all(lambda tag: len(tag.attrs) == 2)
这里，作为参数传入的函数是len(tag.attrs) == 2。当该参数为真时，find_all 函数将返
回tag。即找出带有两个属性的所有标签，如下所示：

```html
<div class="body" id="content"></div>
<span style="color:red" class="title"></span>

```

Lambda 函数非常实用，你甚至可以用它来替代现有的BeautifulSoup 函数：
bs.find_all(lambda tag: tag.get_text() ==
'Or maybe he\'s only resting?')
如果不使用Lambda 函数，代码如下：
bs.find_all('', text='Or maybe he\'s only resting?')

由于Lambda 函数可以是任意返回True 或者False 值的函数，你甚至可以结合使用
Lambda 函数与正则表达式，来查找匹配特定字符串模式的属性的标签。



## 编写

### 遍历单个域名

```python
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
```



导入需要的Python 库之后，程序首先做的是用系统当前时间设置随机数生成器的种子。这样可以保证每次程序运行的时候，维基百科词条的选择都是一个全新的随机路径。然后，程序定义getLinks 函数，它接收一个/wiki/< 词条名称> 形式的维基百科词条URL作为参数，在前面加上维基百科的域名http://en.wikipedia.org，再用该域名的HTML获得一个BeautifulSoup 对象。之后，基于前面介绍过的参数，抽取一列词条链接所在的标签a 并返回它们。程序的主函数首先把起始页面https://en.wikipedia.org/wiki/Kevin_Bacon 里的词条链接列表设置成链接标签列表（links 变量，数据类型为<class 'bs4.element.ResultSet'>）。然后用一个循环，从页面中随机找一个词条链接标签并抽取href 属性，打印这个页面，再把这个链接传入getLinks 函数，重新获取新的链接列表



### 遍历整个网站

遍历整个网站的好处，可以生成网站地图，可以收集数据

连接去重为了避免一个页面被抓取两次，链接去重是非常重要的。在代码运行时，要把已发现的所有链接都放到一起，并保存在方便查询的集合（set）里。集合与列表类似，但是集合中的元素没有特定的顺序，集合只存储唯一的元素，这正是我们需要的功能。只有“新”链接才应被抓取，并从其页面中搜索其他链接：

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()#set() 函数创建一个无序不重复元素集,可进行关系测试,删除重复数据,还可以计算交集、差集、并集等。
def getLinks(pageUrl):
	global pages#定义全局变量
	html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))#打开
	bs = BeautifulSoup(html, 'html.parser')#解释
	for link in bs.find_all('a', href=re.compile('^(/wiki/)')):#遍历a标签下href属性的wiki开头的网站
		if 'href' in link.attrs:#如果href存在与link属性中
			if link.attrs['href'] not in pages:#如果link属性不存在pages中
#We have encountered a new page
				newPage = link.attrs['href']#将属性赋值给newpage
				print(newPage)#打印newpage
				pages.add(newPage)#将newpage加入集合
				getLinks(newPage)#自行调用
getLinks('')#调用函数处理一个空的url，而该空函数实际上就是维基主页面，函数内置了参数
```

如果递归
运行的次数非常多，前面的递归程序很可能会崩溃。

Python 默认的递归限制（程序递归地调用自身的次数）是1000 次。因为维基百科的链接网络浩如烟海，所以这个程序达到递归限制后就会停止，除非你设置一个较大的递归计数器，或者采用其他手段不让它停止。对于那些链接深度小于1000 的“扁平”网站，这种方法通常可行，但有一些罕见的例外。例如，我曾经遇到过一个网站，该网站根据当前网页的地址生成新的URL 链接。这就导致了像blogs/blogs.../blogs/blog-post.php 这样不
断重复的路径。但是大多数时候，这种递归的技巧对于你碰到的任何典型网站都是适用的。

### 抓取整个页面信息

和往常一样，决定如何做好这些事情的第一步就是先观察网站上的一些页面，然后拟定一个抓取模式。通过观察几个维基百科页面，包括词条页面和非词条页面，比如隐私策略页面，就会得出下面的规则。
• 所有的标题（所有页面上，不论是词条页面、编辑历史页面还是其他页面）都是在h1 → span 标签里，而且页面上只有一个h1 标签。
• 前面提到过，所有的正文文本都在div#bodyContent 标签里。但是，如果我们只想获取第一段文字，可能用div#mw-content-text → p 更好（只选择第一段的标签）。这个规则对所有内容页面都适用，除了文件页面（例如，https://en.wikipedia.org/wiki/File:Orbit_of_274301_Wikipedia.svg），它们不包含内容文本（content text）部分。
• 编辑链接只出现在词条页面上。如果有编辑链接，都位于li#ca-edit 标签的li#caedit→ span → a 里面。

调整前面的代码，我们就可以建立一个爬虫和数据收集（至少是数据打印）的组合程序：

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()#设置一个收集集合
def getLinks(pageUrl):
	global pages
	html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
	bs = BeautifulSoup(html, 'html.parser')
	try:
		print(bs.h1.get_text())#.get_text() 会把这些超链接、段落和标签都清除掉，只剩下一串不带标签的文字，提取h1的内容
		print(bs.find(id ='mw-content-text').find_all('p')[0])#查找tag id符合的且时第一段的打印出来
		print(bs.find(id='ca-edit').find('span')
.find('a').attrs['href'])#查找id符合且有span的属性且在a属性下有href的打印出来
	except AttributeError:
		print("页面缺少一些属性！不过不用担心！")#上面有一条没有查找到则打印出来
	for link in bs.find_all('a', href=re.compile('^(/wiki/)')):#遍历页面有a且href属性符合正则表达式的
		if 'href' in link.attrs:#如果href存在，就判断是不是新页面
			if link.attrs['href'] not in pages:#如果link不是新页面
# 我们遇到了新页面
				newPage
    = link.attrs['href']
				print('-'*20)
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)
getLinks('')
```

### 从外链跳转抓取

```python
from urllib.request import urlopen
from urllib.parse import urlparse
# 引入url处理抽取模块，result.scheme : 网络协议; result.netloc: 服务器位置（也有可能是用户信息）;
# result.path: 网页文件在服务器中的位置;result.params: 可选参数;result.query: &连接键值对;result.fragment:
from bs4 import BeautifulSoup
import re
import datetime
import random
pages = set()
random.seed()

# 获取页面中所有内链的列表


def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,
                                  urlparse(includeUrl).netloc)
    # 使用格式化提取url里的scheme(网络协议)，再提取netloc(域名)，组成(网络协议://域名）的格式赋值给变量includeurl
    internalLinks = []  # 创建一个列表
# 找出所有以"/"开头的链接
    for link in bs.find_all('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:  # 判断href是否以及提取过
                if (link.attrs['href'].startswith('/')):  # 如果href以/开头
                    internalLinks.append(  # 则加入internallinks
                        includeUrl + link.attrs['href'])  # 且用原域名加上后面域名
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks  # 返回页面中所有链接
# 获取页面中所有外链的列表


def getExternalLinks(bs, excludeUrl):  # 获取除了自己以外的外部链接
    externalLinks = []
# 找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        # 使用正则表达式获取一个开头是http或者www，且不包含上一个域名的且以以任何字符结尾无论重复几次
        if link.attrs['href'] is not None:  # 提取href如果不是none则
            if link.attrs['href'] not in externalLinks:  # 如果提取的href不在存储过的里面则
                externalLinks.append(link.attrs['href'])  # 把herf添加到存储的后面
    return externalLinks  # 返回存储


def getRandomExternalLink(startingPage):  # 获取随机外部链接
    html = urlopen(startingPage)  # 打开http://oreilly.com
    bs = BeautifulSoup(html, 'html.parser')  # 使用解释器解释
    externalLinks = getExternalLinks(bs, urlparse(
        startingPage).netloc)
    # 提取http://oreilly.com的域名然后传入getExternalLinks，和打开的bs传入，并且返回外链
    if len(externalLinks) == 0:  # 如果外部链接长度等于0那么
        print('没有外链网站，重新获取一个')
        domain = '{}://{}'.format(urlparse(startingPage).scheme,
                                  urlparse(startingPage).netloc)  # 提取协议和域名并插入
        internalLinks = getInternalLinks(bs, domain)  # 使用获取外链函数处理然后赋值给这个
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
        #获取一个随机连接并且返回
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]
        #否则返回一个随即的外部链接


def followExternalOnly(startingSite):  # 传入参数http://oreilly.com
    # 获取随机外链并赋值给externalink,传入参数http://oreilly.com
    externalLink = getRandomExternalLink(startingSite)
    print('随机的外链是: {}'.format(externalLink))  # 打印随机的外链
    followExternalOnly(externalLink)  # 跟随的外链


followExternalOnly('http://oreilly.com')

```

![image-20221115112804941](C:\Users\Mgrsc\Desktop\study\it\programme\pyhton\python_scraping\assets\image-20221115112804941.png)

## 爬虫模型

### 规则和定义对象











## 虚拟环境的使用

虚拟环境可以防止库的冲突，创一个单独的环境来安装库调试程序

```
virtualenv name   #创建一个虚拟环境
source bin/activate #激活虚拟环境
deactive #退出虚拟环境
```

