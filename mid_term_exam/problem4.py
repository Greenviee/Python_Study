def count_mean_over(grade, lst):
    ret = 0
    for i in lst:
        sum = 0
        for j in i:
            sum += j
        avg = sum / 3
        if avg >= grade:
            ret += 1
    return ret