def poldel(a,b):
    l = 0
    r = a
    c=0
    while l <= r:
        m = (r+l)//2
        if m*b<=a:
            c = m
            l = m+1
        else:
            r = m-1
    o = a - c*b
    return c,o

a = int(input())
b = int(input())
if b == 0:
    print('на нуль делить нельзя')
else:
    print(poldel(a,b))