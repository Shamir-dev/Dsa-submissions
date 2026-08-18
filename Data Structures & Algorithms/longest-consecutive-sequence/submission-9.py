class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_count = 1
        seq_count2 = 0

        nums.sort()
        print(nums)

        if not nums:
            return 0
    
        for i in range(1,len(nums)):
             if (nums[i-1] + 1) == nums[i]:
                        seq_count += 1
             elif nums[i-1] == nums[i]:
                        continue
             else:
                   if seq_count2 < seq_count:
                        seq_count2 = seq_count
                   seq_count = 1

        seq_count2 = max(seq_count2, seq_count)

        return seq_count2
            
