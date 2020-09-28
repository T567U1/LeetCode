# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_two_symm(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return is_two_symm(p.left,q.right) and is_two_symm(p.right,q.left)
        return is_two_symm(root,root)
