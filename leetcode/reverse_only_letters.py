"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
"""


class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        My solution: 28ms
        :type S: str
        :rtype: str
        """
        special_char = []
        char = []
        for k,v in enumerate(s):
            if not v.isalpha():
                special_char.append((k, v))
            else:
                char.append((v))
        reverse_str = char[::-1]
        for s in special_char:
            reverse_str.insert(s[0], s[1])
            print(reverse_str)
        return ''.join(reverse_str)


    # def reverseOnlyLetters(self, S):
    #     a = ""
    #     for i in reversed(range(len(S))):
    #         if S[i].isalpha():
    #             a = a + S[i]
    #     a = list(a)
    #     d = [i for i in range(len(S)) if S[i].isalpha() != True]
    #     for i in d:
    #         a.insert(i, S[i])
    #     return ("".join(a))

p = Solution()
# print(p.reverseOnlyLetters("Test1ng-Leet=code-Q!")) #Qedo1ct-eeLg=ntse-T!
# print(p.reverseOnlyLetters("a-bC-dEf-ghIj")) #j-Ih-gfE-dCba
print(p.reverseOnlyLetters("a")) #j-Ih-gfE-dCba
