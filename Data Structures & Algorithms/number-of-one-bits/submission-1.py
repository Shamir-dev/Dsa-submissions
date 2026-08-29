class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
        # count = 0
        # binary = bin(n)[2:]
        # for num in binary:
        #     print(num)
        #     if num == '1':
        #         count +=1

        # return count