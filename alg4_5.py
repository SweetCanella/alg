def f(a):
    if a == 1:
        return a
    elif a%2==0:
        return f(a//2)
    return f((a-1)//2)+f((a//2)+1)

a = int(input())
print(f(a))