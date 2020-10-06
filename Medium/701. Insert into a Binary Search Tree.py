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
'''
    2020-10-06
    class Solution:
        def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
            def go(root, val, head = None):
                if not root:
                    if head.val > val:
                        head.left = TreeNode(val)
                    else:
                        head.right = TreeNode(val)
                    return
                if root.val > val:
                    go(root.left, val, root)
                else:
                    go(root.right, val, root)

            if root:
                go(root, val)
            else:
                root = TreeNode(val)

        return root
    '''
