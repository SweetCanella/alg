def mn(a,b):
    s=[]
    c=0
    x=0
    k=0
    i=0
    o=''
    while True:
        i=a[0]
        if i=='0':
            o=o+'0'
            a.pop(int(i))
        i=b[0]
        if i=='0':
            o=o+'0'
            b.pop(int(i))
        else:
            break
    for i in a:
        for j in b:
            if int(i)*int(j)+c>9:
                s.insert(0,(int(i)*int(j)+c)%10)
                c=(int(i)*int(j)+c)//10
            else:
                s.insert(0,int(i)*int(j)+c)
                c=0
        if c!=0:
            s.insert(0,c)
            c=0
        for l in range(k):
            s.append('0')
        if a.index(i)!=len(a)-1:
            k+=1
        x=x+int(''.join(map(str,s)))
        s=[]
    return str(x)+o

a = list(str(input()))
b = list(str(input()))
a.reverse()
b.reverse()
print(mn(a,b))