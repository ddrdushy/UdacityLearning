def russian_rec(a,b):
    if a == 0:
        return 0
    
    if a % 2 == 0:
        return 2 * russian_rec((a/2),b)
    
    return b + 2 * russian_rec((a-1)/2,b)

print (russian_rec(5,6))
print (russian_rec(7,6))
print (russian_rec(6,6))
print (russian_rec(1,6))