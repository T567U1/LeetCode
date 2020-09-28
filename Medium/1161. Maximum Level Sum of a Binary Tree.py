# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        self.dic = {}
        def get_sum(root, x):
            if not root:
                return
            if x not in self.dic:
                self.dic[x] = root.val
            else:
                self.dic[x] += root.val
            return get_sum(root.right, x + 1), get_sum(root.left, x + 1)
        get_sum(root, 1)

        return max(self.dic, key = self.dic.get)
