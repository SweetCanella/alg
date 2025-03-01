def f(a,sum):
    if a<10:
        sum = sum+a
        return sum
    sum = sum+a%10
    return f(a//10,sum)

a = int(input())
print(f(a,0))