def f(x):
    return 0.25*x**3 + x - 2

def poldel(a,b):
    x = (a+b)/2
    if 0.01 > abs((b-a)/x):
        return x
    if f(x)*f(a)>0:
        return poldel(x,b)
    else:
        return poldel(a,x)
    
print(poldel(0,2))