class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def helper(curr, root)->int:
            if not root:
                return 0

            ans = 0
            temp = curr + root.val

            if not (root.left or root.right):
                return temp

            ans += helper(temp * 2, root.left)
            ans += helper(temp * 2, root.right)

            return ans

        return helper(0, root)
