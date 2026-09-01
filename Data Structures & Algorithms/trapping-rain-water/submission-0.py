class Solution:
    def trap(self, height: List[int]) -> int:
        # define edges case first and last index store none so (first, last)
        #for example 5 elements 1-2, 2-3, 3-4, 4-5 total 4 pairs possible 1 to len(heights)
       if not height:return 0 
       l, r = 0, len(height) - 1 
       leftMax, rightMax = height[l] , height[r] 
       res = 0 

       while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l]) 
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r]) 
                res += rightMax - height[r] 

       return res