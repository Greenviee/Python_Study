pi = 3.141592
def area_and_circumference(r):
    area = pi * r * r
    circumference = 2 * pi * r
    return area, circumference

while 1:
    radius = int(input("반지름을 입력하시오: "))
    if radius < 0:
        print("프로그램을 종료합니다.")
        break
    area, circumference = area_and_circumference(radius)
    print(f"넓이: {area:.3f}, 둘레: {circumference:.3f}")