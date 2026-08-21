# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, low, high): # Helper function with bounds      #BaseCase : empty node is isValid 
            if not node:
                return True 

            #check if node value violates BST property
            if not (low< node.val < high):
                return False 

            #Recursively check left subtree and (upper bound = node.val)
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        #start with infinite bounds 
        return helper(root, float('-inf'), float('inf'))

       