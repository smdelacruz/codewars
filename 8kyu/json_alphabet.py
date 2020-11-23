def correct_polish_letters(st):
    """
    My solution
    There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.
    Your task is to change the letters with diacritics:
    Ex. "Jędrzej Błądziński"  -->  "Jedrzej Bladzinski"
    """
    mapping = {
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ź": "z",
        "ż": "z"
    }
    return "".join(mapping.get(i) if mapping.get(i) else i for i in st)


def correct_polish_letters(s):
    """
    Best solution in codewars
    maketrans : function to translate , should be with equal length
    """
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))





correct_polish_letters("Jędrzej Błądziński")