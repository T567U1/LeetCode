# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.nodes = []
        def get_nodes(root):
            if not root:
                return
            self.nodes += [root.val]
            return get_nodes(root.right), get_nodes(root.left)

        get_nodes(root)
        self.nodes.sort()

        def go(root):
            if not root:
                return
            root.val = sum(self.nodes[self.nodes.index(root.val):])
            return go(root.left), go(root.right)

        go(root)

        return root
