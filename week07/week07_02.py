cache = [-1] * 100
cache[0] = 0
cache[1] = cache[2] = 1

def fibo(n):
    if cache[n] != -1:
        return cache[n]
    else:
        cache[n] = fibo(n - 1) + fibo(n - 2)
        return cache[n]
   
while 1:
    n = int(input("피보나치 값 : "))
    print(f"{fibo(n)}")