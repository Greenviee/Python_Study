day = 0
height = 0
while height < 30:
    if day > 0:
        height -= 5
    day += 1
    height += 7
    print(f"day : {day}     달팽이의 위치 : {height} 미터")
print(f"\n우물을 탈출하는데 걸린 날은 {day}일 입니다.")