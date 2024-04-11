def tax(cost):
    return cost*0.1
def tip(cost):
    return cost*0.18

cost = float(input("식사 비용을 입력하세요: "))
print(f"내야 할 금액 : {(cost + tax(cost) + tip(cost)):.2f}")