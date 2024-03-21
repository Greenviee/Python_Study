num = int(input("숫자를 입력하세요 : "))
isPrime = True
if num == 2:
    print(f"{num}은 소수입니다")
else:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num}은 소수가 아닙니다")
            isPrime = False
            break
    if isPrime:
        print(f"{num}은 소수입니다")