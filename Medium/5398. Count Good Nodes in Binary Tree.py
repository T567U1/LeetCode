# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_ = root.val
        self.count = 0
        def c_val(root, max_):
            if not root:
                return
            max_ = max(root.val, max_)
            self.count += 1 if root.val >= max_ else 0
            return c_val(root.right, max_), c_val(root.left, max_)

        c_val(root, max_)
        return self.count
