class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):#nested function
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1 
                r += 1 
            return s[l+1:r] 
        longest = ""
        for i in range(len(s)):
            #Odd length 
            odd = expand(i, i) 
            if len(odd) > len(longest):
                longest = odd 
            #Even length 
            even = expand(i, i+1) 
            if len(even) > len(longest):
                longest = even 
        return longest 
