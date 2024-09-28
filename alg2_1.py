def f(s):
    return s.index(max(s))

s=[]
for i in range(4):
    a = int(input())
    s.append(a)

while True:
    if s[0] == s[1] == s[2] == s[3]:
        print(s[0])
        break
    else:
        s[f(s)] = max(s) - min(s)

