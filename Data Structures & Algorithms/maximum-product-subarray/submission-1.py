class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0] 
        cur_min = nums[0] 
        result = nums[0] 
        #step 2 iterate throught the array starting from index 1 
        for i in range(1, len(nums)):
            num = nums[i] 
            temp = curr_max 
            curr_max = max(num, num * temp, num * cur_min)
            cur_min = min(num, num * temp, num * cur_min)
            #update the global result 

            result = max(result, curr_max)
        #return the final maximum product 
        return result