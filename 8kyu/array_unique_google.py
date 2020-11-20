

# need to be Unique number

def input1(arr):
    unique_num = list(set(arr))
    missing_items_len = len(arr) - len(unique_num)
    replacement = []
    for i in range(0, missing_items_len):
        sorted_unique_num = sorted(unique_num)
        i += 1
        new_item = sorted_unique_num[-1] + i
        replacement.append(new_item)
    print(sorted_unique_num + replacement)

input1([1000, 5, 5, 6, 5, 5, 5])