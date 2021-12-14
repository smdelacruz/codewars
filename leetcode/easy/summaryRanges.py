"""
Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
Example 3:

Input: nums = []
Output: []
Example 4:

Input: nums = [-1]
Output: ["-1"]
Example 5:

Input: nums = [0]
Output: ["0"]
"""
class Solution:
    def summaryRanges(self, nums):
        """
        my first solution
        """
        # start = None
        # last = None
        # combi = ""
        # result = []
        # if not nums: return result
        # max_arr = nums[-1]
        # print(max_arr)
        # for i in range(max_arr+2):
        #     print(i)
        #     if i in nums:
        #         if start == "":
        #             start = i
        #         else: 
        #             last = i
        #     else:
        #         if last == None and start != None:
        #             combi = "{}".format(start)
        #         elif last != None:
        #             combi = "{}->{}".format(start, last)
        #         if combi != "":
        #             result.append(combi)
        #         start = ""
        #         last = ""
        # return result
        

    def summaryRanges(self, nums):
        """
        my refactored solution
        """
        start = None
        end = None
        result = []
        if not nums: return result
        max_num = nums[-1] 
        for i in range(max_num + 2):
            if i in nums:
                if start == None:
                    start = i
                else: 
                    end = i
            else: 
                if end != None: 
                    result.append("{}->{}".format(start, end))
                else: result.append("{}".format(start))
                start, end = None, None
        return result

p = Solution()
print(p.summaryRanges([0,1,2,4,5,7])) #["0->2","4->5","7"]
print(p.summaryRanges([0,2,3,4,6,8,9])) #["0","2->4","6","8->9"]
print(p.summaryRanges([])) #[]
print(p.summaryRanges([-1])) #["-1"]
