##动物是一个object
class Animal(object):
    pass
##狗是动物
class Dog(Animal):#继承

    def __init__(self, name):
        #狗有名字
        self.name  = name
##猫是动物
class Cat(Animal):

    def __init__(self, name):
        ##猫有名字
        self.name = name
##人是object
class Person(object):

    def __init__(self, name):
        #人有名字和宠物
        self.name = name
        self.pet = None
##佣人是人
class Employee(Person):
    def __init__(self, name, salary):
        ##佣人有名字宠物和工资
        super(Employee, self).__init__(name)#将父类person的init方法运行起来,引入父类的方法
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")#实例化为对象
print(rover.name)
##satan是猫
satan = Cat("Satan")
#mairy是人
mary = Person("Mary")
##mary的宠物叫satan
mary.pet = satan
##frank是佣人
frank = Employee("Frank", 120000)
##frank的宠物是rover
frank.pet = rover
##fliper是鱼
flipper = Fish()
#crouse是salmon
crouse = Salmon()
##harry是hilibut
harry = Halibut()
