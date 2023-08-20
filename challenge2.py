def two_are_positive(a, b, c):
    
    if a > 0 and b > 0 and c > 0:
        return False
    if a > 0 and b > 0:
        return True
    if a > 0 and c > 0 :
        return True
    if b > 0 and c > 0:
        return True
    return False