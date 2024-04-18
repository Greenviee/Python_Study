cache = [0] * 100
cache[0] = 1

def factorial(n):
    if cache[n] != 0:
        return cache[n]
    else:
        cache[n] = factorial(n - 1) * n
        return cache[n]
    
while 1:
    n = int(input("팩토리얼 값 : "))
    print(f"{factorial(n)}")