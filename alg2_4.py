p = int(input())
s = 4
k = 1
m = 2**p -1
while (k != p-1):
    s = ((s*s)-2)%m
    k+=1
if s == 0:
    print('простое')
else:
    print('составное')
