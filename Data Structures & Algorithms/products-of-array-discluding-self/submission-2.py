class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # defined the different cases No -zero Atleast zero or multiple
        count_zero = 0
        products = 1
        res = []
        position = 0
        for i in range(len(nums)):
            if count_zero > 1:
                 break
            if nums[i] == 0:
                count_zero += 1
                position = i
                continue
            products *= nums[i]



        if count_zero == 0:
            # for i in range(len(nums)):
            #     products *= nums[i]
            for num in nums:
                res.append(int(products/num))
            return res



        elif count_zero == 1:
              for i in range(len(nums)):
                if i == position:
                    res.append(products)
                    continue
                res.append(0)

        else: res = [0]*len(nums)
        return res