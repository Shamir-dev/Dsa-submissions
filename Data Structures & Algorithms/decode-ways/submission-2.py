class Solution:
       def numDecodings(self, s: str) -> int:
        dp = {len(s): 1} 

        def dfs(i):
            if i in dp:
                return dp[i] 
            if s[i] == "0":
                return 0 
            
            res = dfs(i+1) 
            if (i+ 1 < len(s) and (s[i] == "1" or 
                s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            dp[i] = res 
            return res 

        return dfs(0)



















#       def max_num(self,nums: list):

#         count = 0
#         candidates = None 
#         for num in nums:
#             if count == 0:
#                 candidates = num 
#             if num == candidates:
#                 count += 1
#             else:
#                 count -= 1 
#         return candidates 
# sol = Solution()

# print(sol.max_num(['a','b','a','a','b']))