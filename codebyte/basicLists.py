li = [1,5,16, 100, -199]
li.pop()
print(li) #result: [1,5,16, 100]
print(li.append(-2)) #result: [1,5,16, 100]
# li.reverse()
# print(li) #[-199, 100, 16,5,1]
# print(li.reverse()) #None (I dont know why; google reason "it does reverse in place of the list and returns None."")
# print(list(reversed(li))) ##[-199, 100, 16,5,1]


"""
Challenge: check if characters is sorrounded by + sign +y+ = true
inputs:
+d+=3=+s+ #true 3 is not a letter
f++d+ # false

"""

# def plusSign(words):
#     """
#     codebyte solution
#     """
#     words = "=" + words + "=" #solution to avaoid indexError
#     li = list(words)

#     for i in range(0, len(li)):
#         if li[i].isalpha():
#             if li[i-1] != "+" or li[i+1] != "+":
#                 return False
#     return True

# print(plusSign("f++fp")) #false
# print(plusSign("+d+=3=+s+")) # true