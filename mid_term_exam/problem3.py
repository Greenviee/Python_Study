def pascal_triangle(n):
    if n == -1:
        return []
    if n == 0:
        return [1]
    lst = []
    for i in range(n + 1):
        if i == 0 or i == n:
            lst.append(1)
        else:
            lst.append(pascal_triangle(n - 1)[i - 1] + pascal_triangle(n - 1)[i])
    return lst