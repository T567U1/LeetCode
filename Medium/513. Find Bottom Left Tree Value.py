# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        dic = {}
        def go(root, level):
            if not root:
                return
            if root:
                if (level + 1) in dic:
                    dic[level + 1].append(root.val)
                else:
                    dic[level + 1] = [root.val]

            return go(root.left, level + 1) , go(root.right, level + 1)

        go(root, 0)
        return dic[max(dic)][0] if dic else root.val
