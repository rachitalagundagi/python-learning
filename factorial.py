import time

def factorial(num):
    start = time.time()
    c = 1
    for i in range(1,num):
        c *= i+1
    end = time.time()
    print(end - start)
    return c

def fact(num):
    start = time.time()
    c = 1
    while(num>0):
        c*=num
        num-=1
    end = time.time()
    print(end - start)
    return c

def facts(n):
    if n <= 1:
        return [1]    
    last = facts(n-1)
    return last + [n * last[-1]]



# print(factorial(4))
# print(fact(4))
start = time.time()
print(facts(4)[-1])
end = time.time()
print(end-start)