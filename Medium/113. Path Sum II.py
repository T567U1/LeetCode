# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self.ans = []
        def go(root, arr = []):
            if not root:
                return

            arr += root.val,

            if not root.left and not root.right and sum(arr) == target:
                self.ans += arr[:],

            go(root.left, arr)
            go(root.right, arr)

            arr.pop()

        go(root)

        return self.ans
