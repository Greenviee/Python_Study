src = "aaaabccccaaaaacccfg"
output = ""
i = 0
while i < len(src):
    ch = src[i]
    output += ch
    cnt = 0
    while i < len(src) and ch == src[i]:
        cnt += 1
        i += 1
    output += str(cnt)
print(output)