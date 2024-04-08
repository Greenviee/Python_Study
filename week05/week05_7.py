def unit_fraction(frac):
    i = 2
    while (1 / i) > frac:
        i += 1
    if abs(1 / i - frac) > abs(1 / (i - 1) - frac):
        return i -1
    else:
        return i

frac = float(input("1보다 작고 0보다 큰 소수를 입력하세요: "))
answer = unit_fraction(frac)
print(f"가장 가까운 단위 분수는 1/{answer}이며, 이 값은 {1 / answer}입니다.")