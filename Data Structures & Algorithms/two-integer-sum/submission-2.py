class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = []
        for i in range(len(nums)):
          for j in range(i, len(nums)):
            if nums[i] + nums[j] == target and i != j: 
                return [i,j]
               

        # hashmap = {}
        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in hashmap:
        #         return [hashmap[diff], i]
        #     hashmap[num] = i
