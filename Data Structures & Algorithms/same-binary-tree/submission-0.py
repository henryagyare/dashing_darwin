# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        if p.val != q.val:
            return False

        # left side:
        left_valid = self.isSameTree(p.left, q.left)

        # right side:
        right_valid = self.isSameTree(p.right, q.right)

        return left_valid and right_valid


        # return self.isSameTree(p.left, q.left) == self.isSameTre(p.right, q.right)