def solve(arr):
    count = 0
    new_arr = []
    for words in arr:
        for i, v in enumerate(words, 1):
            alphabet_position = ord(v.lower())-96
            if i == alphabet_position:
                count += 1
        new_arr.append(count)
        count = 0   



""""

def solve(arr):
    return [ sum(c == chr(97+i) for i,c in enumerate(w[:26].lower())) for w in arr ]
"""
print(solve(["abode","ABc","xyzD"]))
