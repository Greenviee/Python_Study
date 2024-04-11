def discount(bread):
    return 3.49 * 0.6 * bread

bread = int(input("구매한 하루 된 빵의 개수를 입력하세요: "))
print(f"정상 가격 : {bread * 3.49:.3f}, 할인된 금액 : {discount(bread):.3f}, 총 가격 : {bread * 3.49 - discount(bread):.3f}")