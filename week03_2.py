x, y = input("점의 좌표를 입력하세요 (x, y) : ").split()
x = int(x)
y = int(y)
if x > 0:
    if y > 0:
        print("1사분면")
    else:
        print("4사분면")
else:
    if y > 0:
        print("2사분면")
    else:
        print("3사분면")