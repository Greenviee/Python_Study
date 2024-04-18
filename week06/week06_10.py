def get_solution(a, b, c):
    D = b * b - 4 * a * c
    if D < 0:
        print(f"{a}x^2 + {b}x + {c} = 0의 실근은 0개입니다.")
        return
    s1 = (-b + (b * b - 4 * a * c)**(1/2)) // (2 * a)
    s2 = (-b - (b * b - 4 * a * c)**(1/2)) // (2 * a)
    if s1 == s2:
        print(f"{a}x^2 + {b}x + {c} = 0의 실근은 {s1} 1개입니다.")
    else:
        print(f"{a}x^2 + {b}x + {c} = 0의 실근은 {s1}, {s2} 2개입니다.")

a, b, c = input("이차방정식을 입력하세요 : ").split()
a = int(a)
b = int(b)
c = int(c)
get_solution(a, b, c)
