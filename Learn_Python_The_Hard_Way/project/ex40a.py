#字典  将一种东西对应到另外一种的方式
mystuff = {'apple': "i am apples"}#apple(key),i ma pple(value)
print(mystuff['apple'])

#模块(module)
#1.包含函数和变量的python文件
#2.可以导入这个文件
#3.然后可以使用.操作符访问模块中的函数和变量
def apple():
    rpint("I am apples")
tangerine = "living reflection of a dream"

import mystuff
#调用mystuff.py这个模块,可以把他当作字典，他可以存放python代码并通过.运算符访问这些代码
mystuff.apple()#访问apple函数,语法（.key)
print(mystuff.tangerine)

#类  通过类可以把一组函数和数据放到一个容器中，从而用.运算符访问
#和module一样有一个导入的方法叫实例化(instantiate),当将一个类实例化之后就得到一个叫对象的(object)
class MyStuff(object): #可以用这个类重复创建出很多来，
    def __init__(self):#__init__有这个魔法函数则调用该函数对空对象self初始化
        self.tangerine = "And now a thousand years"#初始化空对象里的tangerine

    def apple(self):
        print("i am classy apples")

thing = MyStuff() #将类实例化,类似迷你导入，并赋值给变量thing 类似于套用Mystuff框架建好一个叫thing的房子
thing.apple()#调用实例化后的类（即对象）里的apple函数
print(thing.tangerine)#将MyStuff摸具套到thing上
