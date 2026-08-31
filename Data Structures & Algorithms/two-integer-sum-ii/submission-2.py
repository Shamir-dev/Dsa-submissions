class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {} #this is a dictionay to store element as key and its indices as Value
        res = [] # result store in "res" list
        for i in range(len(numbers)):
            required = target - numbers[i]
            if required in seen:
                res.extend([seen[required]+1, i+1])
                break

                
            if numbers[i] in seen:
                pass 
            else:
                seen[numbers[i]] = i 


        return res