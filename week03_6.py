n = int(input("n을 입력하시오 : "))

for i in range(1, n + 1):
    if (i % 2) == 1:
        for j in range(1, n + 1):
            print(f"{n * (i - 1) + j}", end = " ")
    else:
        for j in range(0, n):
            print(f"{n * (i) - j}", end = " ")
    print("\n")