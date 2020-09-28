# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0

        def go(root, d = 0):
            if not root:
                return []

            left = go(root.left, d + 1)
            right = go(root.right, d + 1)

            for l in left:
                for r in right:
                    if l - d + r - d <= distance:
                        self.ans += 1

            r_depth = left
            r_depth.extend(right)

            if root.left is root.right == None:
                r_depth += d,

            return r_depth

        go(root)

        return self.ans

            
