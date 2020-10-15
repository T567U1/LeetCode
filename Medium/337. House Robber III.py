# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def go(root):
            if not root:
                return [0,0]

            left = go(root.left)
            right = go(root.right)

            stealval = root.val + left[1] + right[1]
            notstealval = max(left) + max(right)

            return [stealval, notstealval]

        return max(go(root))
        
