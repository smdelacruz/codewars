
class Solution:
    def singleNumber(self, nums):
        """
        my first solution
        """
        exist_arr = []
        for i in nums:
            if i not in exist_arr:
                exist_arr.append(i)
            elif i in exist_arr:
                exist_arr.remove(i)
        return exist_arr[0]

        
p = Solution()
print(p.singleNumber([0,0,4])) #4
# print(p.singleNumber([0])) #4
        