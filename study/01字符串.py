def wc(n, s=''):
    if n == 0:
        print(s)
    else:
        wc(n-1, s+'0')
        wc(n-1, s+'1')

wc(5)
