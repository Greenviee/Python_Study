def reverse_input(s, i, ret):
    if i == len(s):
        return ret
    ret += s[len(s) - i - 1]
    return reverse_input(s, i + 1, ret)

def reverse_input2(s):
    if len(s) <= 1:
        return s
    return reverse_input2(s[1:]) + s[0]

s = str(input("문자열 입력 : "))    
print(reverse_input(s, 0, ""))