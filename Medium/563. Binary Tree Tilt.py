# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        def go(root):
            if not root:
                return 0
            else:
                left = go(root.left)
                right = go(root.right)
                self.ans += abs(left - right)
                return root.val + left + right
        go(root)
        return self.ans
