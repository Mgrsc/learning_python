import math

def prime_factors(n):
    """返回一个整数n的所有质因子"""
    factors = []
    while n % 2 == 0:  #先把质因数2提取出来
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def factorize_interval(a, b):
    """打印区间[a,b]内所有整数的分解"""
    for i in range(a, b+1):
        factors = prime_factors(i)
        print(f"{i}=", end="")
        for j in range(len(factors)):
            print(factors[j], end="")
            if j != len(factors)-1:
                print("*", end="")
        print()
a,b = map(int,input().split())
factorize_interval(a,b)

