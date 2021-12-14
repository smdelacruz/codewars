"""
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1
"""
class Solution:
    def maxPower(self, s):
        """
        my solution
        """
        if len(s) == 0: return None
        counter = 1
        max_value = 1
        current_letter = s[0] 
        # for i in range(1, len(s)):
        for i in s[1:]: #refactor
            if current_letter == s[i]:
                counter += 1
                max_value = max(counter, max_value)
            else:
                if counter > max_value:
                    max_value = counter
                current_letter = s[i]
                counter = 1
        return max_value

    # def maxPower(self, s):
    #     """
    #     other leetcode solution
    #     """
    #     power = [1] * len(s) #[1,1,1,1,1....]
    #     curr_char = s[0]
    #     for i in range(1, len(s)):
    #         if curr_char == s[i]:
    #             power[i] = power[i - 1] + 1
    #             print(power[i])
    #             print(power[power[i - 1] + 1])
    #         else:
    #             curr_char = s[i]
        
    #     return max(power)


    def maxPower(self, s):
        """
        other leetcode solution
        , same as Mine but refactored. better
        """
        prev = s[0]
        count = 1
        power = 1
        for char in s[1:]:
            if prev == char:
                count += 1
                power = max(count, power)
            else:
                prev = char
                count = 1
        return power

p = Solution()
print(p.maxPower("abbcccddddeeeeedcba")) #5
print(p.maxPower("hooraaaaaaaaaaay")) #11
print(p.maxPower("cc")) #11
# print(p.maxPower("")) #11