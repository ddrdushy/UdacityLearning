def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

print (naive(5,6))
print (naive(7,6))
print (naive(6,6))
print (naive(1,6))
