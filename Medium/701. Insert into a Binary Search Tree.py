# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert_(root, val):
            if not root:
                return
            if root.val < val:
                if root.right == None:
                    root.right = TreeNode(val)
                else:
                    insert_(root.right, val)
            else:
                if root.left == None:
                    root.left = TreeNode(val)
                else:
                    insert_(root.left, val)

        insert_(root, val)
        return root if root else TreeNode(val)
