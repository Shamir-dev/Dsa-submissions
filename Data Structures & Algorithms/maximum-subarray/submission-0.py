class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # form given an array find the maximum sum of subArray example
        # arr = [ 2, -3, 4, 2,-2, 1,-1,4]  maxSum = 8
        maxSum = nums[0]
        curSum = 0 

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n 
            maxSum = max(maxSum, curSum)
        return maxSum