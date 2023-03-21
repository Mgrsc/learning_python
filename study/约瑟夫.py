import random

lst = [(i+1, random.randint(1, 5)) for i in range(int(input('请输入人数：')))]
print(f'生成的编号和密码为：{lst}')

#初始化
suiji_num = random.randint(1, 5)
print(f'生成的初始随机数为: {suiji_num}')
output_lst = [] #新建一个列表存储输出
zz = 0 #初始化一个指针g
 
while len(lst) > 0:
    # 报数
    zz = (zz + suiji_num - 1) % len(lst) #指针等于（指针加上密码-1后取列表长度的模）,核心算法
    output_lst.append(lst.pop(zz))
    suiji_num = output_lst[-1][1] if lst else suiji_num #判断lst是否为空，不空则取上一个的密码，空则弹出循环

print(f"出圈顺序：{output_lst}")
