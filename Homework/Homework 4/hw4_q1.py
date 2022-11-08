a = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 11, 12, 13, 14, 16, 15, 17, 18, 18]
b = list(range(20))

def listdiff(a, b):
    dif = []
    i = 0
    for x in a:
        if x != b[i]:
            dif = dif + [i]
        i +=1
    return dif
