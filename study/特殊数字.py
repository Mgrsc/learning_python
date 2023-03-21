import math
a = []
for i in range(100,1000):
    i = str(i)
    a.append(i)

for b in a:
    b = int(b)
    c100 = b // 100
    c10 = b// 10%10
    c1 = b %10
    if sum([int(math.pow(c100,3)), int(math.pow(c10,3)), int(math.pow(c1,3))]) == b:
        print(b)
