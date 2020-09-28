# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        arr, arr1 = [], []
        def gl(root, arr):
            if not root:
                return
            elif root.left == None and root.right == None:
                return arr.append(root.val)
            return gl(root.left, arr), gl(root.right, arr)
        gl(root1, arr)
        gl(root2, arr1)

        return arr == arr1
        
