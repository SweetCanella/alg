def plus(a,b):
    s=''
    c=0
    for i in range(len(a)-1,-1,-1):
        x = int(a[i]) + int(b[i]) + c
        c=0
        if x > 9:
            s = str(x-10) + s
            c+=1
        else:
            s = str(x) + s
    return s

def minus(max,min):
    s=''
    c=0
    for i in range(len(max)-1,-1,-1):
        x = int(max[i]) - int(min[i]) - c
        c=0
        if x < 0:
            s = str(x+10) + s
            c+=1
        else:
            s = str(x) + s
    return s



a = list(str(input()))
p = str(input())
b = list(str(input()))
while len(a) != len(b):
    if len(a) > len(b):
        b.insert(0,'0')
    else:
        a.insert(0,'0')
max = a
min = b
if int(''.join(a))<int(''.join(b)):
    max = b
    min = a
if p == '+':
    print(plus(a,b))
if p == '-':
    print(minus(max,min))
else:
    print('не тот символ бро')