src = "a2b3c6a2c3f1g1"
output = ""
for i in range(0, len(src)-1, 2):
    for j in range(int(src[i+1])):
        output += src[i]
print(output)