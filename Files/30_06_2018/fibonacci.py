#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    curr = 0
    after = 1
    
    for i in range(0,n):
        curr,after = after, curr + after
        
    return curr

print (fibonacci(0))
#>>> 0
print (fibonacci(1))
#>>> 1
print (fibonacci(15))
#>>> 610
print (fibonacci(36))
#>>> 14930352