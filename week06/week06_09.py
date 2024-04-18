def color(loc):
    if (loc[0] == 'a') or (loc[0] == 'c') or (loc[0] == 'e') or (loc[0] == 'f'):
        if int(loc[1]) % 2 == 0:
            return "흰색"
        else:
            return "검은색"
    else:
        if int(loc[1]) % 2 == 0:
            return "검은색"
        else:
            return "흰색"
        
locate = str(input("체스판의 좌표를 입력하세요 : "))
print(f"{locate}는 {color(locate)} 칸입니다.")