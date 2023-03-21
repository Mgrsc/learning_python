def xun(zi):
    i = 0
    numbers = []
    while i < zi: ## i<6时循环打印
        print(f"at the top i is {i}")
        numbers.append(i) #在numbers后面添加每次循环的i变量
        i = i + 1
        print ("number now :", numbers)
        print(f"at the bottom i is {i}")
    return numbers


zi = int(input(">"))#注意input返回的类型是str不能直接比较要转为数字
numbers = xun(zi) #必须将函数返回值赋值给变量，不可直接使用函数内返回值
print("the number:")
for num in numbers:
    print(num)
