def f(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return f(b,a%b)
    return f(a,b%a)

a = int(input())
b = int(input())
print(f(a,b))
