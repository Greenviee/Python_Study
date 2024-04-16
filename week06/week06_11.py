def Tomohiko(y):
    return (y + (y - 1) // 4 - (y - 1) // 100 + (y - 1) // 400) % 7

year = int(input("연도를 입력하세요 : "))
day_list = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
print(f"{year}년 1월 1일은 {day_list[Tomohiko(year)]}입니다.")