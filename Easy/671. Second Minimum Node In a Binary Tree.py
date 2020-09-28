# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans = set()
        def go(root):
            if not root:
                return
            self.ans.add(root.val)
            return go(root.left), go(root.right)
        go(root)
        return sorted(self.ans)[1] if len(self.ans) > 1 else -1
