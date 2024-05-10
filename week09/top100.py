#파일 읽기
def read_csv(filename):
    f = open(filename, "r", encoding="utf-8")
    content = f.readlines()
    return content.split(",")

get_csv = read_csv("20240502_melon_top100.csv")
print(get_csv)