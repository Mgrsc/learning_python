#输入一个数转为int，再用hex转为16进制截取后两位转化为可读在转化为大写并打印
print(str(hex(int(input()))[2:]).upper())
#upper将小写转化为大写
