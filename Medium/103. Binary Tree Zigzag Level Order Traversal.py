# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = {}
        def go(root, level):
            if not root:
                return
            if level in self.ans:
                self.ans[level] += root.val,
            else:
                self.ans[level] = [root.val]

            return go(root.left, level + 1), go(root.right, level + 1)

        go(root, 0)

        ans = []
        f = False

        for node in self.ans:
            if not f:
                ans += self.ans[node],
            else:
                ans += self.ans[node][::-1],
            f = True if not f else False

        return ans
