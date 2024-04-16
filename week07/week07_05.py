def take(n, lst):
    if n <= 0 or not lst:
        return []
    else:
        ret = [lst[0]]
        return ret + take(n-1, lst[1:])
    
lst = [1,2,3,4,5]
print(f"{take(3, lst)}")