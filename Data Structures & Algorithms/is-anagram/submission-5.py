class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = False
        # if len(s)==len(t):
            # count = 0;
            # for i in range(len(s)):
            #     for j in range(len(t)):
            #         result = False
            #         if s[i]==t[j]:
            #             result = True
            #             count +=1
            #             break
            #     if count == i:
            #         break
            # sList = list(s)
            # tList = list(t)
            # new_sList = sList.sort()
            # new_tList = tList.sort()
            # print(sList)
            # print(tList)
            # if sList == tList:
            #     result = True

        return sorted(s)== sorted(t)