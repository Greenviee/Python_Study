n = int(input("n을 입력하시오 : "))

map = []
#map = [1, 2, ... , n]
for i in range(n*n):
    map.append(i+1)
#짝수번째만 reverse해서 출력
for i in range(n):
    new_s = map[i*n:(i+1)*n]
    if i % 2 == 0:
        print(new_s)
    else:
        new_s.reverse()
        print(new_s)