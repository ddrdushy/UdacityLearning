def russian(a,b):
    x,y,z=a,b,0
    while x>0:
        if x % 2 == 1:
            z = z + y
        y = y << 1
        x = x >> 1
    return z

print (russian(5,6))
print (russian(7,6))
print (russian(6,6))
print (russian(1,6))