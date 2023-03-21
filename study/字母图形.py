n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        print(chr(ord('A') + abs(i-j)), end='')
    print()
