arr = []
def disappeared_numbers(a):
    arr=set(a)
    return [i for i in range(1,len(a)+1) if i not in arr]