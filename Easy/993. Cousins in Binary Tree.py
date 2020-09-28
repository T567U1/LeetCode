# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.keys = {}

        def go(root, level, parend):
            if not root:
                return
            if root.val == x or root.val == y:
                # record of level and parend
                self.keys[root.val] = {'level' : level, 'parend' : parend}
            return go(root.left, level + 1, root.val), go(root.right, level + 1, root.val)

        go(root, 0, root.val)

        if len(self.keys) < 2:
            return False

        return self.keys[x]['level'] == self.keys[y]['level'] and self.keys[x]['parend'] != self.keys[y]['parend']
            
