def findodd(num_list):
    sum = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            sum += num_list[i]
    return sum

slist = input("숫자 리스트를 입력하세요: ")
nlist = list(map(int, slist.split(',')))
print(f"홀수들의 합: {findodd(nlist)}")