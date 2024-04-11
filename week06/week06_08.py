def isodd(num):
    return num % 2

num = int(input("정수를 입력하세요 : "))
if isodd(num):
    print(f"{num}은 홀수입니다.")
else:
    print(f"{num}은 짝수입니다.")