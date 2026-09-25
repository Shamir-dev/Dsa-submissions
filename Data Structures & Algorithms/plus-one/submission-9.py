class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        if n == 0 and digits[n] == 9:
                digits[n] = 0
                digits = [1] + digits
                return digits
        if digits[n] == 9:
            digit = digits[n] 
            while digit == 9:
                if digits[n-1] < 9:
                    digits[n] = 0
                    digits[n-1] = digits[n-1] + 1
                    return digits
                digits[n] = 0
                digit = digits[n-1]
                n = n-1
                if n == 0 and digits[n] == 9:
                    digits[n] = 0
                    digits = [1] + digits
                    return digits
        else:
            digits[n] = digits[n] + 1

        return digits