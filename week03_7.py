print("세 자리의 암스트롱 수 : ", end="")

for i in range(1, 10):
    for j in range(i, 10):
        for k in range(j, 10):
            num = i*i*i + j*j*j + k*k*k
            if (num) >= 100 and (num) < 1000:
                print(num, end=" ")