"""
Given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
"""


class Solution:
    def maximum69Number(self, n):
        max = n
        num = str(n)

        for digit in range(len(num)):
            print("digit", digit)
            print("num[digit]", num[digit])
            if num[digit] == "6":
                print("if")
                newdigit = num[digit].replace("6", "9")
            else:
                print("else")
                print("b4 ", num[digit])
                newdigit = num[digit].replace("9", "6")
                print("after ", newdigit)
            num = newdigit
            print("new num",num)
            max = max if max >= int(num) else int(num)
            print("max", max)
            num = num
            print("num", num)

        return max

p = Solution()
print(p.maximum69Number(9))
# print(p.maximum69Number(9996))
