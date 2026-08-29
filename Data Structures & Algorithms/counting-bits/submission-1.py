class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [] 

        for i in range(n+1):
            binaryC = bin(i).count("1")
            output.append(binaryC)
        return output
