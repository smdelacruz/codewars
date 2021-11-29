def isPangram(pangram):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    result = ""
    value = 1
    for sentences in pangram:
        remove_sent_space = sentences.split(" ")
        sent_to_list = list(set("".join(remove_sent_space)))
        for letter in alphabet:
            if letter not in sent_to_list:
                value = 0
                break
            else:
                value = 1
        result += str(value)
    return result
    

# print(isPangram("pack my box with five dozen liquor jugs"))
print(isPangram(["we promptly judged antique ivory buckles for the next prize",
"we promptly judged antique ivory buckles for the prizes",
"the quick brown fox jumps over the lazy dog", 
"the quick brown fox jump over the lazy dog" ]))