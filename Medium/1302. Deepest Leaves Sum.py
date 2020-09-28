# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.sum_ = {}
        self.max_ = 0
        def get_root(root, floor):
            if not root:
                return
            self.max_ = max(self.max_, floor)
            if floor in self.sum_:
                self.sum_[floor] += root.val
            else:
                self.sum_[floor] = root.val

            return get_root(root.left, floor + 1), get_root(root.right, floor + 1)

        get_root(root, 1)
        return self.sum_[self.max_]
                
