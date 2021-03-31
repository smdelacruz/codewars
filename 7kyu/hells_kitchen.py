"""
Gordon Ramsay shouts. He shouts and swears. There may be something wrong with him.

Anyway, you will be given a string of four words. Your job is to turn them in to Gordon language.

Rules:

Obviously the words should be Caps,
Every word should end with '!!!!', Any letter 'a' or 'A' should become '@', Any other vowel should become '*'.
"""
def gordon(a):
    """
    My Solution
    """
    gordon_words = ""
    for i in a:
        if i == "a":
            gordon_words += "@"
        elif i in "eiou":
            gordon_words += "*"
        elif i == " ":
            gordon_words += "!!!! "
        else:
            gordon_words += i.upper()
    return gordon_words + "!!!!"


def gordon(a):
    """
    My Solution using translate as a practice
    """
    return "!!!! ".join(a.translate(a.maketrans("aeoui", "@****"))

def gordon(a):
    """
    BEst answer
    """
    return '!!!! '.join(a.upper().split()).translate(str.maketrans('AEIOU', '@****'))+'!!!!'


print(gordon('are you stu pid'))
print(gordon('i am a chef'))
