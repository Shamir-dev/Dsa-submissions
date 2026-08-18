class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Lowercase
        s = s.lower()
        
        # Step 2: Remove non-alphanumeric characters
        cleaned = re.sub(r'[^a-z0-9]', '', s)
        
        # Step 3: Reverse and compare
        return cleaned == cleaned[::-1]
        
        # newStr = "".join(s)
      
        # while right > left:
        #     if s[left] != s[right]:
        #         result = False
        #         break
        #     left += 1
        #     right -= 1

      
    