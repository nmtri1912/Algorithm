# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left,right):
            if(left is None and right is None):
                return True
            if((left is None and right!=None) or (left!=None and right is None)):
                return False
            if(left.val!=right.val):
                return False
            if(not helper(left.left,right.right) or not(helper(left.right,right.left))):
                return False
            return True
            
        
        if(root is None):
            return True
        left = root.left
        right = root.right
        return helper(left,right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricTest(self, p , q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        return self.isSymmetricTest(p.left, q.right) and self.isSymmetricTest(p.right, q.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isSymmetricTest(root.left,root.right)

