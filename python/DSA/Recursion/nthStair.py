def stair(n):
    if n<=2:
        return n
    a=1
    b=2
    for i in range(3,n+1):
        current = a+b
        a=b
        b=current
    return b

print(stair(2))
