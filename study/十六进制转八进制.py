n=int(input())
list1=[]
for i in range(n):
    list1.append(input())
for i in range(n):
    result=oct(int(list1[i], 16))
    print(result[2:])
