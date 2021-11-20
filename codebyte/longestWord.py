import re

def LongestWord(sen):

    # p = sen.split(" ")
    onlyString = re.sub('[^A-Za-z0-9 ]+', '', sen)
    return max(onlyString.split(" "), key=len)

    # for i in p.split(" ") if len(i) > len(longest) 
    # for i in p:
    #     # stripString = i.strip("!&@#$%^&*(),.:}{~/")
    #     stripString = re.sub('[^A-Za-z0-9 ]+', '', i)
    #     if len(stripString) >= len(longest):
    #         longest = stripString
    # return longest


# keep this function call here 
print(LongestWord("a confusing /:sentence:/[ this is not!!!!!!!~"))