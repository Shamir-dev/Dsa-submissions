class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{","]":"["}

        for ch in s:
            if ch in mapping:
                #closing bracket
                if not stack or stack[-1] != mapping[ch]:
                    return False
                
                stack.pop()
            else: #opening bracket
                stack.append(ch)

        return not stack
        # left = 0
        # right = len(s) -1
        # replicate = []
        # result = True
        # while left < right:
        #     if s[left] == '(':
        #         replicate.append(')')

        #     elif s[left] == '{':
        #         replicate.append('}')

        #     elif s[left] == '[':
        #         replicate.append(']')
        #     else:
        #         replicate.append(s[left])
        #     print(replicate)
          
        #     if replicate[left] ==  s[right]:
        #         left +=1
        #         right -=1
        #     else:
        #         return False
        # return result