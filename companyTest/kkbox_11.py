def solution(S):
    char_holder = ""
    str_len = len(S)
    counter = 0
    c = 0
    highest = 0
    for i in range(str_len):
        print("-------")
        if S[i] != char_holder:
            char_holder = S[i]
            counter = 1
            c += 1
            print("current", char_holder)
            print("counter", counter)
            print("c", c)
        elif S[i] == char_holder and counter < 2:
            counter += 1
            c += 1
        elif S[i] == char_holder and counter >= 2:
            highest = c
        # print("S", S[i])
        # print("c", c)
        # print("pairs", pairs)
        # print("h
        # ighest", highest)
    return highest
        


# def solution(S):
#     temp = ""
#     counter = 1
#     consec_counter = 0
#     holder = 0
#     str_len = len(S)
#     # for i in S:
#     print(str_len)
#     for i in range(str_len):
#         print("-------")
#         print("i", S[i])
#         if S[i]!=temp:
#             print("if") 
#             temp = S[i]
#             counter = 1
#             consec_counter +=1
#         elif counter < 2:
#             print("elif") 
#             counter += 1
#             consec_counter += 1

#         elif counter >=2 and i != str_len-1: 
#             counter = 1
#             if S[i+1] != temp:
#                 consec_counter = 1
#                 holder +=1
#         print("temp", temp)
#         print("counter", counter)
#         print("consec_counter", consec_counter)
#         print("holder", holder)
#     return consec_counter + holder



print(solution("baaabbabbb")) #aabbabb --> 7
print(solution("abaaaa")) #abaa --> 4