
class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
          return ""
        sizes, res = [] ,[] #initializes empty dictonary/array./list

        for s in strs:
             # example let have str = "Fuck this coding & programming "
            sizes.append(len(s)) 
            # here it stores char sizes ofeach wordas sizes[4,4,6,1,11]
        print(sizes)
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
    
        sizes, res, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        
        return res


