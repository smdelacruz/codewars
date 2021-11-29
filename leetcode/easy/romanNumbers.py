def romanToInt(s):
    symbols = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    counter = 0
    string_len = len(s)
    deduct = 0
    for i in range(string_len):
        i_2 = string_len - i - 1 #AWESOME
        romanNumeralValue = symbols[s[i_2]]
        
        if s[i_2] in ["V", "X"]:
            if s[i_2-1] == "I":
                counter += romanNumeralValue - 1
            else: counter += romanNumeralValue
        elif s[i_2] in ["L", "C"]:
            if s[i_2-1] == "X":
                counter += romanNumeralValue - 10
            else: counter += romanNumeralValue
        elif s[i_2] in ["D", "M"]:
            if s[i_2-1] == "C":
                counter += romanNumeralValue - 100
            else: counter += romanNumeralValue
        else: 
            counter += romanNumeralValue
    return counter
print(romanToInt("III")) #3
print(romanToInt("IV")) #4
print(romanToInt("LVIII")) #58
print(romanToInt("MCMXCIV")) #1994