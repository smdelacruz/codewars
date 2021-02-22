class Solution:
    def reverse(self, x: int) -> int:
        number = int(str(abs(x))[::-1])
        if abs(number) < 2 ** 31 and number != -2**31 - 1:
            return number if x > 0 else -number
        else: return 0


p = Solution()
print(p.reverse(1563847412))
