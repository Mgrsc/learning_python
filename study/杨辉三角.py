n = int(input())

a = [1]
for i in range(n):
    print(' '.join(map(str, a)))
    a = [1] + [a[j]+a[j+1] for j in range(len(a)-1)] + [1]
