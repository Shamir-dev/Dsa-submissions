class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 

        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= goal:
                goal = i 
        return True if goal == 0 else False  

        # first = nums[0]
        # i = 0
        
        # def jump(self, i )-> bool:
        #     nextIndex = nums[i]
        #     nextPos = nums[nextIndex]
        #     i = nextIndex 
        #     if i == len(nums) -1:
        #         return True 
        #     if nums[i] == 0  :
        #         return False
        