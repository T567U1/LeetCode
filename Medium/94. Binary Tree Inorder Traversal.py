# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []
        def go(root):
            if not root:
                return
            go(root.left)
            self.ans += root.val,
            go(root.right)


        go(root)

        return self.ans
