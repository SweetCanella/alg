def x(n):
    if n == 0 or n == 1:
        return 1
    return (x(n-1))+(x(n-2))

print(x(10))