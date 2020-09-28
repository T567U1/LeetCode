# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = {}
        def go(root, level):
            if not root:
                return
            if level in self.ans:
                self.ans[level] += root.val,
            else:
                self.ans[level] = [root.val]

            return go(root.left, level + 1), go(root.right, level + 1)

        go(root, 0)

        return [self.ans[nodes] for nodes in self.ans]
            
