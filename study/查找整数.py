n=int(input());l=list(map(int,input().split()));a=int(input())
c = [i+1 for i in range(n) if l[i] == a]
print(c[0] if c else -1)
