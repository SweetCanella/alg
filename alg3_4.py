def mn(a,b):
    s=''
    c=0
    



a = list(str(input()))
b = list(str(input()))
while len(a) != len(b):
    if len(a) > len(b):
        b.insert(0,'0')
    else:
        a.insert(0,'0')
