a = int(input())
b = list(map(int,input().split()))
c = []
while len(b) != 1:
    b = sorted(b)
    e = b.pop(0)
    b= sorted(b)
    f = b.pop(0)
    b.append(e+f)
    c.append(e+f)
print(sum(c))

