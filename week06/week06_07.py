def sum(num):
    return int(num*(num+1) / 2)

num = int(input("양의 정수를 입력하세요 : "))
print(f"1부터 n까지의 합 : {sum(num)}")