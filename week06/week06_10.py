def solution(a, b, c):
    disc = b*b - 4*a*c
    if disc < 0:
        print(f"{a}x^2 + {b}x + {c} = 0의 실근은 존재하지 않습니다.")
        return
    s1 = (-b + (b*b - 4*a*c)**(1/2)) / (2*a)
    s2 = (-b - (b*b - 4*a*c)**(1/2)) / (2*a)
    if disc == 0:
        print(f"{a}x^2 + {b}x + {c} = 0의 실근은 {s1} 한 개 입니다.")
    else:
        print(f"{a}x^2 + {b}x + {c} = 0의 실근은 {s1}, {s2} 두 개 입니다.")
    

a, b, c = input("이차방정식의 계수를 입력하세요 : ").split()
a = int(a)
b = int(b)
c = int(c)
solution(a, b, c)