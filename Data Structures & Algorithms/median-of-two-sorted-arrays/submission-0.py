class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0 
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1 
        # Add the leftovers 
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1 
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1 
        print(merged)
        #define two cases for median i)  odd simple mid values and ii) even average of two mid values 
        if len(merged) % 2 == 1:
            return merged[(len(merged)//2)]
        else: 
            return (merged[(len(merged)//2)] + merged[(len(merged)//2) -1])/2


        
       

