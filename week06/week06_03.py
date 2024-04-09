def listmulti(num_list):
    ret = 1
    if len(num_list) == 0:
        return 0
    for i in range(len(num_list)):
        ret *= num_list[i]
    return ret

string = input("숫자 리스트를 입력하세요: ")
nlist = list(map(int, string.split(',')))
print(f"리스트 원소들의 곱: {listmulti(nlist)}")