import random
a = random.randint(10000,99999)
print(a)
for i in range(9):
    a = str(a*a)
    n = (len(a)-5)//2
    a = int(a[n:n+5])
    print(a)