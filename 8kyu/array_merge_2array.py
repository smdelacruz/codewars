def merge_arrays(arr1, arr2):
    """
    my sotlution.
    set() - will remove duplicate
    list - array
    """
    return list(dict.fromkeys(arr1+arr2))


def merge_arrays(arr1, arr2):
    """
    Best solution by the other warriors in codewars
    """
    return sorted(set(arr1+arr2))


merge_arrays([1, 2, 3, 4, 4, -6, -9], [5, 6, 7, 8, -8, -9, -6])
merge_arrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12])