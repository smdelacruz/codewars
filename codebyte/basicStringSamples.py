helloString = "hello world I am coding"
lookfor = "I"

print(helloString.find(lookfor)) #result:12 (position)
print(helloString[helloString.find(lookfor):]) #result: I am coding (print all string after the find )
print(helloString[helloString.find(lookfor):18]) #result: I am c (print position of find to index 18)
print(helloString.title()) #result: Hello World I Am Coding (capitalize first letter in words)
print(helloString.istitle()) #result: False (check if string has Capitalized format)
print(list(helloString)) #result: ['h', 'e', 'l'...] (make all letters as an array including space)
print(helloString.swapcase()) #(swap the cases of chars from lower <> upper)