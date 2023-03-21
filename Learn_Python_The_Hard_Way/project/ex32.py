#Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。https://www.runoob.com/python/python-for-loop.html
#range(start, stop[, step])
#参数说明：
#start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
#stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
#step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"this is count {number}")

for fruit in fruits:
    print(f"A fruit or type: {fruit}")

for i in change:
    print(f"i go {i}")

elements = []

for i in range(0, 6): #0-5没有6
#Python3 range() 返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表，
    print(f"adding {i}to the list.")
    elements.append(i)#append() 方法用于在列表末尾添加新的对象。每次循环都在elements列表里添加一个数

for i in elements:
    print(f"element was: {i}")
