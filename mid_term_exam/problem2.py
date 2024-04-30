def is_find_element_in_matrix(lst, target):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == target:
                return True
    return False