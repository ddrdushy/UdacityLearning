import time

def execution_time(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result,run_time

def spin_loop(n):
    i = 0
    while i < n:
        i = i+1


print(execution_time("spin_loop(10**9)")[1])