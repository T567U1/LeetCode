# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = True
    def isBalanced(self, root: TreeNode) -> bool:

        def are_you_balance(root):
            if not root:
                return 0
            left = are_you_balance(root.left)
            right = are_you_balance(root.right)
            print(left, right)
            if abs(left - right) > 1:
                self.ans = False
            return max(left, right) + 1

        are_you_balance(root)
        return self.ans
    
