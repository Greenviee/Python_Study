string = str(input("쉼표로 구분된 정수를 여러 개 입력하시오: "))
strlist = string.split(',')
intlist = list(map(int, strlist))
print(f"입력된 정수의 리스트: {intlist}")
intlist.sort()
print(f"정렬된 정수의 리스트: {intlist}")