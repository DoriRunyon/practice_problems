
"""
>>> A = [1, 2, 5, 6, 8]
>>> B = [0]
>>> C = [1, 5, 6, 77, 88, 456, 789, 1000]
>>> D = [-6, -5, 0, 1, 6, 77, 88, 456, 789, 1000]

>>> search(A, 5)
True
>>> search(A, 0)
False
>>> search(B, 0)
True
>>> search(B, 9)
False
>>> search(C, 456)
True
>>> search(C, 1000)
True
>>> search(C, 1)
True
>>> search(C, -9)
False
>>> search(D, -5)
True
>>> search(D, -9)
False

"""

def search(lst, n):

    while len(lst) > 1:
        mid = len(lst)/2
        if n == lst[mid]:
            return True
        elif n < lst[mid]:
            lst = lst[:mid]
        else:
            lst = lst[mid:]

    if lst[0] == n:
        return True
    else:
        return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"

