# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Helper function to check if two trees are identicals
        def isSameTree(s, t):
            #case 1 : both trees are empty -> they match
            if not s and not t:
                return True 
            
            #case 2: one is empty and the other is not -> mismatch
            if not s or not t: 
                return False 
            
            #case 3: values differ-> mismatch 
            if s.val != t.val:
                return False 

            #case 4: value match-> check left and right children recursively 
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

          
       #main logic :traverse root tree
        if not root:
                return False # if root is empty , no subtree possible
             # step1: check if current node's subtree matches  subRoot 
        if isSameTree(root, subRoot):
                return True 
            #step2: Otherwise ,keep searching in left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        