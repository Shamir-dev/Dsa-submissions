class Solution:
    def rob(self, nums: List[int]) -> int:
        # we can start from fist or second house no problem we can rob equal number of house
        rob1, rob2 = 0,0 

        for n in nums:
            temp = max(n + rob1, rob2) 
            rob1 = rob2 
            rob2 = temp 
        return rob2 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
        # sumOdd,sumEven,sum1,i, sum2, j = 0,0,0,0,0,1
        # if len(nums)%2 == 0:
        #     #Rob Even index house ie 0,2,4,like that 
        #     while i < len(nums):
        #         sum1 = sum1 + nums[i]
        #         i+=2
        #     while j < len(nums):
        #         sum2 = sum2 + nums[j]
        #         j+= 2
        #     sumEven = max(sum1,sum2)
            
        # else:
        #     while i < len(nums):
        #         sum1 = sum1 + nums[i]
        #         i+=2
        #     while j < len(nums):
        #         sum2 = sum2 + nums[j]
        #         j+= 2
        #     sumOdd = max(sum1,sum2)
        # return max(sumOdd, sumEven)




            


                
