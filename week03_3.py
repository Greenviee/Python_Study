num = int(input("1에서 9까지의 수를 입력하세요: "))
while (num < 1) or (num > 9):
    num = int(input("1에서 9까지의 수를 다시 입력하세요: "))

for i in range(1, 10):
    print(f"{num} * {i} = {num * i}")