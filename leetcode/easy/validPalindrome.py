class Solution:
    def isPalindrome(self, s):
        """
        my solution
        """
        # new_s = "".join(i.lower() for i in s if i.isalnum())
        # return new_s == new_s[::-1]


        """
        other solution 98% faster, 
        """
        print(filter(str.isalnum, s))
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        return s == s[::-1]

p = Solution()
print(p.isPalindrome("A man, a plan, a canal: Panama"))
# print(p.isPalindrome("  "))
# print(p.isPalindrome("race a car"))
        
      
        