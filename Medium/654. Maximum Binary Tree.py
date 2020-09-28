# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        #create root
        root = TreeNode(max(nums))

        def go(nums, root):
            if not nums:
                return

            index_ = nums.index(max(nums))
            if nums[: index_]:
                root.left = TreeNode(max(nums[: index_]))

            if nums[index_ + 1:]:
                root.right = TreeNode(max(nums[index_ + 1:]))

            return go(nums[: index_], root.left), go(nums[index_ + 1:], root.right)

        go(nums, root)

        return root
