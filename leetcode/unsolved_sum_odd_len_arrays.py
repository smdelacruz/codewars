"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
A subarray is a contiguous subsequence of the array.
Return the sum of all odd-length subarrays of arr.
Example 1:
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
"""

class Solution:
    """
    Other leet code solution
    """
    def sumOddLengthSubarrays(self, arr):
        ans = 0
        for i in range(1, len(arr) + 1, 2): #get the index of all odd
            for j in range(len(arr)): #count
                print("i{},j{},j+i--{}".format(i,j,j+i))
                if (j + i) <= len(arr): #
                    print("arr[j:j + i]==", arr[j:j + i])
                    ans += sum(arr[j:j + i])
        return ans

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        Observations :
        each element is present once in odd length of 1 sub-array , and sum of these arrays = sum(arr)
        eache element a[i] is present in 3 sub-arrays of lenght 3 : [a[i], a[i+1], a[i+2]] , [a[i-1],a[i], a[i+1]] , , [a[i-2],a[i-1],a[i]] , all but the a[0] which is present in 1 array a[0],a[1],a[2] , a[1] which is present in 2 arrays a[0],a[1],a[2] and ,a[1],a[2],a[3] and same for the other end of the array a[n-2] - is present in 2 arrays, a[n-1] is present in 1 array a[n-3],a[n-2],a[n-1] . Sum of this arrays is 3 * sum(arr) - missing elements 2 * a[0] + a[1] + a[n-2] + 2 * a[n-1]
        on a general case for row k : sum = k*sum(arr) - (k-1) * a[0] - (k-2)*a[1] .....- (k-2)*a[n-2] - (k-1)*a[n-]
        """
        row = sum(arr)
        r = 0
        delta = 0
        minus = 0
        for i in range(len(arr)):
            if i % 2 == 0:
                r += row * (i + 1) - minus
            delta += arr[i] + arr[len(arr) - 1 - i]
            minus += delta
        return r

p = Solution()
print(p.sumOddLengthSubarrays([1,4,2,5,3])) # 58
print(p.sumOddLengthSubarrays([1,2])) # 3