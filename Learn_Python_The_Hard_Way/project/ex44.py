###隐式继承
class Parent(object):
    def implicit(self):
        print("PARENT implict()")

class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

#显示覆盖
#隐式覆盖无法让子类里的函数有不同的行为。
class parent(object):
    def override(self):
        print("PAREMENT override()")

class child(parent):
    def override(self):
        print("CHILD override()")#需要覆盖子类中的函数，只要在子类中定义一个同名函数就可以

dad = parent()
son = child()
dad.override()
son.override()



## 在运行前或运行后替换
class arent(object):
    def altered(self):
        print("PARENT altered()")

class hild(arent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(hild, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = arent()
son = hild()
dad.altered()
son.altered()




##组合使用
class rent(object):
    def override(self):
        print("PARENT override")
    def implicit(self):
        print("PARENT implicit()")
    def altered(self):
        print("PARENT altered()")

class ild(rent):
    def override(self):##覆盖
        print("CHILD override()")

    def altered(self):

        print("CHILD, BEFORE PARENT altered()")
        super(ild,self).altered()
        print("CHILD, after paprent alterred()")


dad = rent()
son = ild()

dad.implicit()
son.implicit()##隐式
dad.override()
son.override()##显示覆盖
dad.altered()
son.altered()##特殊覆盖super调用
