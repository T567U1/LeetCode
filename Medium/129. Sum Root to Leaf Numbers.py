# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = []
        def go(root, s = ''):
            if not root:
                return

            s += str(root.val)
            if not root.left and not root.right:
                self.ans += int(s),

            go(root.left, s)
            go(root.right, s)
            s = s[:-1]

        go(root)

        return sum(self.ans)
