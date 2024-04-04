def cel2fah(cel):
    fah = cel * 1.8 + 32
    return fah

for i in range(5):
    cel = (i + 1) * 10
    print(f"섭씨 : {cel}, 화씨 : {cel2fah(cel)}")