# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.dic = {}

        def go(root, level):
            if not root:
                return
            self.dic[level] = root.val
            return go(root.left, level + 1), go(root.right, level + 1)

        go(root, 0)

        return list(self.dic.values())
