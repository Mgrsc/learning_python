n = int(input())
l = []
for i in range (10000,1000000):
    a = str(i)
    if a == a[::-1]:
        l.append(i)

for k in l:
    if sum(list(map(int,str(k))))==n:
        print(k)


