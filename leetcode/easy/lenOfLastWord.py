class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])


p = Solution()
print(p.lengthOfLastWord("   fly me   to   the moon  "))
        
        