class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return [] 
        n = len(nums)
        result = [] 
        deq = deque() 

        for i in range(n):
            #remeove element that not within the sliding windows 
            while deq and deq[0] < i - k + 1:
                deq.popleft() 
            #remove smaller element from the deque 
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop() 
            #add currennt element index to the deque 
            deq.append(i)

            #The maximum element at the front of the deque 
            if i >= k -1 :
                result.append(nums[deq[0]])
        return result