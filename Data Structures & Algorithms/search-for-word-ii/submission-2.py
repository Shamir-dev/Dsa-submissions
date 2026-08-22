class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # store word at end node
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #build TrieNode
        root = TrieNode()
        for w in words:
            cur = root 
            for c in w: 
                if c not in cur.children: 
                    cur.children[c] = TrieNode() 
                cur = cur.children[c] 
            cur.word = w 

        rows, cols = len(board), len(board[0]) 
        res = [] 

        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 
            if board[r][c] == "#": #already visited
                return 
            ch= board[r][c]
            if ch not in node.children:
                return 

            cur = node.children[ch] 
            if cur.word:
                res.append(cur.word) 
                cur.word = None #avoide duplicates
            board[r][c] = "#" # mark -visited 
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r+dr, c+dc, cur) 
            board[r][c] = ch # restore] 

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res
        