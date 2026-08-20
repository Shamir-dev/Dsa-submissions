# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Fuck the coding....
        if not root:
            return 0
        depthL = self.maxDepth(root.left)#this shit of lines count left nodes depth suppose we have to nodes left and right firstly it calculate max depth amongst all of child nodes at left sides
        depthR = self.maxDepth(root.right)

        max_depth = 1 + max(depthL,depthR)
        return max_depth
        