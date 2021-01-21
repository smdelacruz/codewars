def merge_arrays(arr1, arr2):
    """
    my sotlution.  incomplete
    set() - will remove duplicate
    list - array
    """
    print(list(set(arr2) - set(arr1)))
    print(set(arr2) - set(arr1))
    print(list(arr1 + list(set(arr2) - set(arr1))))
    # return sorted(list(arr1 + list(set(arr2) - set(arr1))))



merge_arrays([1, 2, 3, 4], [5, 6, 7, 8])
merge_arrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12])