def reverseWords(s):
    """
    My Solution
    reverses all of the words within the string passed in.
    :param s: Sentence ex. "hello world!"
    :return: world! hello
    """
    split_by_space = s.split(' ')
    return ' '.join(split_by_space[::-1])


def reverseWords(s):
    """
    Other people solution from codeWars
    """
    return ' '.join(reversed(s.split(' ')))


reverseWords("hello world!")