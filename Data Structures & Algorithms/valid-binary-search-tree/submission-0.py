# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            # left child
            leftChildBound = left   # -inf
            rightChildBound = node.val  # 2, 
            validLeft = valid(node.left, leftChildBound, rightChildBound)    # ()

            # right child
            leftChildBound = node.val
            rightChildBound = right
            validRight = valid(node.right, leftChildBound, rightChildBound)

            return validLeft and validRight


        return valid(root, -math.inf, math.inf)