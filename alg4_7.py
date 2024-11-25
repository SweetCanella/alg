h = [[] for _ in range(7)]
print(h)
s = [86, 90, 27, 29, 38, 30, 40]
c=0
while c != len(s):
    for i in s:
        index = i%7
        if h[index] == []:
            h[index] = i
            c+=1
        else:
            while True:
                index += 1
                if index == len(s):
                    index = 0
                if h[index] == []:
                    h[index] = i
                    c+=1
                    break
print(h)