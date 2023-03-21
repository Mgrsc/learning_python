n = int(input())
f1, f2 = 1, 1
if n == 1:
    print(1%10007)
elif n == 2:
    print(1%10007)
else:
    for i in range(3, n+1):
        f3 = (f1 + f2) % 10007
        f1, f2 = f2, f3
    print(f3)
