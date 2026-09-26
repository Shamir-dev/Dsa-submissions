class Solution:
    def myPow(self, x: float, n: int) -> float:
        product = 1
        if x == 1 or n == 0 :
            return 1
        elif x == -1:
            if n % 2  == 1:
                return -1
            else: return 1
        elif n > 0:
            for i in range(n):
                product = product * x

            return product
        elif n< -10000:
            return 0
        else :
            for i in range(n,0):
                product = product * x
            return 1/product
        