import re
def QuestionsMarks(strParam):
    new_string = re.sub('[^0-9???]',"", strParam)
    print(new_string)
    hello = [int(s) for s in new_string if s.isdigit()]
    print(len(hello))
    print((len(hello) % 2) == 0)
    if (len(hello) % 2) == 0:
        it = iter(hello)
        new_list = [a+b for a,b in zip(it, it)]
        return all("10" in str(i) for i in new_list)
    else: return False
    
    
# keep this function call here 
print(QuestionsMarks("acc?7??sss?3rr1??????5"))
print(QuestionsMarks("aa6?9"))