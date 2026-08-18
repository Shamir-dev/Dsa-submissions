class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for  num in nums:
            count[num] = count.get(num, 0) + 1
            #sort number by their frequency highest first
        sorted_nums = sorted(count, key= count.get, reverse= True)

            #Return the k most frequent numbers
        results = sorted_nums[:k]

        return results



    #qustion , Given a Dumb integer Array "nums" and integer'k' Now we have to return 'k' most frequent element within this array
        # results =[]
        # for i in range(len(nums)):
        #     count =1
        #     for j in range(i, len(nums)):
        #         if nums[i] == nums[j] and i != j:
        #             count +=1
        #     if count >= k:

        #         results.append(nums[i])

        
        # return list(set(results))