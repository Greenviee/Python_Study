for i in range(1, 10001):
    sum = 0
    div = []
    for j in range(1, i):
        if i % j == 0:
            sum += j
            div.append(j)
    if sum == i:
        print(f"{i}는 완전수입니다")
        print(f"{i}의 약수 : {div}, 약수의 합 : {sum}")
