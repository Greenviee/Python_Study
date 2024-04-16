def pow(x, n):
    if n == 0:
        return 1
    # 느림
    # return x * pow(x, n - 1)
    # n이 커지면 위 방식으로 풀면 시간제한 걸릴 수 있음
    if n % 2 == 0:
        half_pow = pow(x, n // 2)
        return half_pow * half_pow
    else:
        half_pow = pow(x, n // 2)
        return half_pow * half_pow * x

print(f"{pow(9, 3)}")