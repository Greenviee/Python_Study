num = str(input("정수를 입력하세요 : "))
length = len(num)
isInverted = True

for i in range(0, length // 2):
    if num[i] != num[length - i - 1]:
        isInverted = False
        break
if isInverted:
    print(f"{num}은 거꾸로 정수입니다.")
else:
    print(f"{num}은 거꾸로 정수가 아닙니다.")