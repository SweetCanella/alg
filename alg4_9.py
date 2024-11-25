def f(a):
    a = list(a)
    l = set(a)
    s={}
    for i in l:
        s[i]=a.count(i)
    print(s)

a = input()
f(a)