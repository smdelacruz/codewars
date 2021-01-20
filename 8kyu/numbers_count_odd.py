def odd_count(n):
    """
    oddCount(7) //=> 3, i.e [1, 3, 5]
    oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]

    My soltuion, too slow
    """
    odd = [i for i in range(n) if i % 2 != 0]
    return len(odd)


def oddCount(n):
    """
    Best solution
    note: //: divide with integral result (discard remainder)
    """
    return n // 2

oddCount(15)
oddCount(15023)
