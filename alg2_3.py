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


def Ferm(n):
    m = int(n**0.5)
    x = 1
    while True:
        q = (m + x)**2 - n
        if int(q**0.5) == q**0.5:
            break
        else:
            x+=1
    b = q**0.5
    a = m+x
    p = int(a+b)
    q = int(a-b)
    return list((p,q))

n = 19691