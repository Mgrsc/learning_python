#Python 字典 items() 方法以列表返回视图对象，是一个可遍历的key/value 对。
#dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。
#视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。
#我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
#list() 方法用于将元组或字符串转换为列表。
#dict.get(key[, value]) :字典 get() 函数返回指定键的值。key -- 字典中要查找的键。value -- 可选，如果指定键的值不存在时，返回该默认值。
states = {  #创建字典
    'oregon': 'or',
    'Florida': 'fl',
    'california': 'ca',
    'new york': 'ny',
    'michigan': 'mi'
}

cities = {  #创建字典
    'ca': 'san francisco',
    'mi': 'detroit',
    'fl': 'jacksonville',
}

cities['ny'] = 'new york'   #加入cities字典
cities['or'] = 'portland'

print('-' * 10)
print("ny state has: ", cities['ny']) #取出cities字典
print("or state has: ", cities['or'])

print('-' * 10)
print("michigan's abbreviation is: ", states['michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print("michigan has: ", cities[states['michigan']]) #先取出states字典中的再取出cities字典中的
print("Florida has: ", cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()): #items将states字典取出为视图对象将视图对象转化为列表，且赋值给前两个变量，for遍历对象
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):#itmes将字典转换为视图对象再转化为列表，for遍历列表并赋值
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('texas')#字典 get() 函数返回指定键的值。

if not state: #if取真not取反
    print("soory, no texas")

city = cities.get('tx', 'does not exist') #
print(f"the city for the state 'tx' is:{city}")
