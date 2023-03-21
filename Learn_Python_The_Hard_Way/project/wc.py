class MyStuff(object):  # 可以用这个类重复创建出很多来，
    def __init__(self):  # __init__有这个魔法函数则调用该函数对空对象self初始化
        self.tangerine = "And now a thousand years"  # 从self中取出tangerine赋值

    def apple(self):
        print("i am classy apples")


thing = MyStuff()  # 将类实例化为对象
thing.apple()  # 调用对象，通过.运算符取出apple函数
print(thing.tangerine)  # 调用对象，通过.运算符取出tangerine函数
