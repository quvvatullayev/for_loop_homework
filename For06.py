def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    s = 0
    x = list(range(A,B))
    for i in x:
        if type(i) == type(5):
            while i != 0:
                s += i%10
                i //= 10
    return s

print(main(-6,8))