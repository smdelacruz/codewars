import re
# def QuestionsMarks(strParam):
#     """
#     my solution
#     """
#     new_string = re.sub('[^0-9???]',"", strParam)
#     print(new_string)
#     hello = [int(s) for s in new_string if s.isdigit()]
#     print(len(hello))
#     print((len(hello) % 2) == 0)
#     if (len(hello) % 2) == 0:
#         it = iter(hello)
#         new_list = [a+b for a,b in zip(it, it)]
#         return all("10" in str(i) for i in new_list)
#     else: return False
    
def QuestionsMarks(strParam):
    """
    Correct solution
    """
    a = 11
    b = 'false'
    c = 0
    for i in strParam:
        print("i", i)
        if i.isdigit():
            if int(i) + a == 10:
                print("if", int(i) + a)
                if c != 3:
                    return 'false'
                b = 'true'
            c = 0
            a = int(i)
        elif i == '?':
            c += 1
            print("c", int(c))
    return b
     
# keep this function call here 
print(QuestionsMarks("acc?7??sss?3rr1??????5"))
print(QuestionsMarks("aa6?9"))