def birthday(num):
    year = num[0] + num[1]
    month = num[2] + num[3]
    day = num[4] + num[5]
    if int(year) < 51:
        year = "20" + year
    else:
        year = "19" + year
    print(f"{year}년 {month}월 {day}일")

string = str(input("주민등록번호 첫 6숫자 형식 입력: "))
birthday(string)