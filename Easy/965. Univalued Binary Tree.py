# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        def get_val(root):
            if not root:
                return True
            return get_val(root.right) and get_val(root.left) and root.val == val

        return get_val(root)
