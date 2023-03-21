# def functionname( parameters ):
#   "函数_文档字符串"
#   function_suite
#   return [expression]

#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
#str.encode(encoding='UTF-8',errors='strict')：以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
#str.decode(encoding='UTF-8',errors='strict')：以 encoding 指定的编码格式解码字符串。默认编码为字符串编码。
#str.split(str="", num=string.count(str)).:过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
#sorted(iterable, cmp=None, key=None, reverse=False)：对所有可迭代的对象进行排序操作。
#list.pop([index=-1]):函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

import sys #提出软件包
script, filename = sys.argv #使用软件包里argv方法
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()


print(f"So, you're {age} old, {height} tall and {weight} heavy.")



txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

def txt_again_read(file_again):
    file_again.read()
    return file_again

print(txt_again_read(txt_again))#可用向函数直接传递变量也可数字也可数学表达式


print('Let\'s practice everything.')
print("""You\'d need to know \'bout escapes
      with \\ that do \n newlines and \t tabs.""")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)#直接传递变量给函数，将变量给函数调用函数并将返回的变量赋值给前三个

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))#插入变量，且该变量收集所有参数



people = 20
cats = 30
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")


def print_two(*args): #*告诉python把函数的所有参数都接收进来，然后放到名叫args的列表中去
        arg1, arg2 = args   #解包
        print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):  #可用跳过解包过程，直接把参数写在parameters
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):  #函数一个参数
    print(f"arg1: {arg1}")

def print_none():  #函数可用不接受参数
        print("i go nothin'.")

print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("first")
print_none()
