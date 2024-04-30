def sum_of_odd(lst):
    sum = 0
    for i in lst:
        if i == -1:
            return 0
        if i % 2 == 1:
            sum += i
    return sum