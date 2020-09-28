# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert_leaf(root):
            if not root:
                return
            temp_left = root.left
            temp_right = root.right
            root.left = temp_right
            root.right = temp_left
            invert_leaf(root.right)
            invert_leaf(root.left)
            
        invert_leaf(root)

        return root
