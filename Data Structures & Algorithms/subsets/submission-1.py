class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 

        def backtrack(index, subset):
            if index == len(nums):
                result.append(subset[:]) # stores a copy 
                return 
                # indclude current element 
            subset.append(nums[index]) 
            backtrack(index + 1, subset) 

                #Exclude current element 
            subset.pop() 
            backtrack(index + 1, subset) 
        backtrack(0, []) 
        return result

        