num1 = int(input("정수를 입력하세요 : "))
num2 = int(input("정수를 입력하세요 : "))
num3 = int(input("정수를 입력하세요 : "))
if num1 < num2:
    if num2 < num3:
        print(num1, num2, num3)
    else:
        if num1 < num3:
            print(num1, num3, num2)
        else:
            print(num3, num1, num2)
else:
    if num1 < num3:
        print(num2, num1, num3)
    else:
        if num2 < num3:
            print(num2, num3, num1)
        else:
            print(num3, num2, num1)
