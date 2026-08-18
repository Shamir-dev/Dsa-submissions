class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        width = right - left
        max_area = 0
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = width * height

            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area

        # totalPossiblity = []
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         distance = j -i
        #         Area =  distance * min(heights[i], heights[j])
        #         totalPossiblity.append(Area)

        # return max(totalPossiblity)