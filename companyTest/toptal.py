def firstRepeatedWord(sentence):
    repeated = []
    words = sentence.split(" ")
    print(words)
    for i in words:
        if i == "":
            pass
        elif i in repeated:
            return i
        else:
            repeated.append(i)



print(firstRepeatedWord("He had had quite enough of this nonsense."))
print(firstRepeatedWord("that       that occurs"))