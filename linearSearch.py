def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

print linearSearch([14, 15, 6, 27, 13, 16, 25, 11, 7], 15)
