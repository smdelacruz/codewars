def distinct(seq):
    new_seq = []
#     for s in seq:
#         if s not in new_seq:
#             new_seq.append(s)
#     return new_seq

    return [new_seq.append(s) for s in seq if s not in new_seq]


print(distinct([1]))
print(distinct([1, 1, 1, 2, 3, 4, 5]))