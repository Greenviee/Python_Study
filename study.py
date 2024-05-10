def take(lst, n):
    if n <= 0 or not lst:
        return []
    else:
        ret = [lst[0]]
        ret += take(lst[1:], n - 1)
    return ret
    

nlist = [1,2,3,4,5]
print(take(nlist, 4))