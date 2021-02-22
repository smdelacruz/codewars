books = "Release Date: December 8, 2020 [EBook #63984], Language: German, Character set encoding: " \
        "UTF-8 *** START OF THIS PROJECT GUTENBERG EBOOK AUS PRAGER GASSEN UND NÄCHTEN ***"


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE
    print(file_contents)
    new_dict = {}
    remove_punc = "".join(i for i in file_contents if i not in punctuations)
    separatee_string = remove_punc.split(" ")
    for i in separatee_string:
        word = i.lower()
        if not word.isalpha() or word in uninteresting_words:
            continue
        if word.isalpha():
            new_dict[word] = 0
        new_dict[word] += 1
    print(new_dict)
    # for i in file_contents:
    #     if i not in punctuations:
    #         new_string += i
    #     print(new_string)
#         else: print("exist in new_dict")
# wordcloud


print(calculate_frequencies(books))