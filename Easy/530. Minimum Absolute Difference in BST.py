# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.keys = []
        ans = float('inf')
        def go(root):
            if not root:
                return
            self.keys += [root.val]
            return go(root.left), go(root.right)

        go(root)
        self.keys.sort()
        for x, y in zip(self.keys, self.keys[1:]):
            ans = min(y - x, ans)

        return ans
        
