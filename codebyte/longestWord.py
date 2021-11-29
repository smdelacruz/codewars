import re

def LongestWord(sen):
    onlyString = re.sub('[^A-Za-z0-9 ]+', '', sen)
    return max(onlyString.split(" "), key=len)
    
# keep this function call here 
print(LongestWord("a confusing /:sentence:/[ this is not!!!!!!!~"))