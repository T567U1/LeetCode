# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        self.ans = {}
        self.a = True
        if not root.val & 1:
            return False

        def go(root, level):
            if not root or not self.a:
                return

            if level in self.ans:
                if level % 2 == 0:
                    if self.ans[level][-1] >= root.val or not root.val & 1:
                        self.a = False
                else:
                    if self.ans[level][-1] <= root.val or root.val & 1:
                        self.a = False

                self.ans[level] += root.val,

            else:
                if not level & 1 and not root.val & 1:
                    self.a = False
                if level & 1 and root.val & 1:
                    self.a = False
                self.ans[level] = [root.val]

            go(root.left, level + 1)
            go(root.right, level + 1)

        go(root, 0)

        return self.a
        
