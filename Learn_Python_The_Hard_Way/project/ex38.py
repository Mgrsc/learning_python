#str.join(sequence)：用于将序列中的元素以指定的字符连接生成一个新的字符串。
ten_things  = "apples organges crowstelephone light sugar"
print("wait therer are not 10 thing in that list let fix that")

stuff = ten_things.split(' ') #根据特定字符切片
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"] #创建列表

while len(stuff) !=10: #循环#len() 方法返回对象（字符、列表、元组等）长度或项目个数。stuff变量的长度不等于10循环
    next_one = more_stuff.pop()#移除列表中最后一个元素并返回
    print("adding:", next_one)
    stuff.append(next_one)##append() 方法用于在列表末尾添加新的对象。
    print(f"there are {len(stuff)} items now")

print("there we go: ", stuff)

print("let's do some things with stuff")

print(stuff[1])#stuff列表第二个
print(stuff[-1])#stuff列表最后一个
print(stuff.pop())#移除最后一个打印
print(' '.join(stuff))#加入一个
print('#'.join(stuff[3:5]))#从索引为三直到索引为四，五不算，用于将序列中的元素以指定的字符连接生成一个新的字符串。
