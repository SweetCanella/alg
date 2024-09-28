def SimpleNumbers(n):
    s=[i for i in range(2,n+1)]
    j=0
    a=[]
    while True:
        p = s[j]
        a = [s[i] for i in range(len(s)) if s[i]%p!=0]
        a.insert(0,p)
        if sorted(s) == sorted(a):
            return sorted(s)
            break
        else:
            s = a
            j+=1

n = int(input())
s = ''
for i in SimpleNumbers(n):
    c = 0
    a = n
    while a>0:
        if a%i==0:
            c+=1
            a = a//i
        else:
            if c>0:
                s = s+ str(i)
                if c>1:
                    s = s+'^'+str(c)
                s = s+'*'
            break

print(s[:-1])