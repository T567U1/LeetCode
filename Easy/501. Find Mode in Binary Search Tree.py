# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.dic = {}
        def go(root):
            if not root:
                return
            if root.val in self.dic:
                self.dic[root.val] += 1
            else:
                self.dic[root.val] = 1

            return go(root.right), go(root.left)

        go(root)
        ans = []
        max_ = max(self.dic, key =self.dic.get)
        for key in self.dic:
            if self.dic[key] == self.dic[max_]:
                ans.append(key)

        return ans
            
