# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        def go(root, max_, min_):
            if not root:
                return
            max_ = max(max_, root.val)
            min_ = min(min_, root.val)
            self.ans = max(self.ans, max_- min_)
            return go(root.right, max_, min_), go(root.left, max_, min_)
        go(root, 0, 100 * 10)
        return self.ans
