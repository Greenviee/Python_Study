def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(16):
    print(f"fibo({i:4d}) = {fibonacci(i):8d}")