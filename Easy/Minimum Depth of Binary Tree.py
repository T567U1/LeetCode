class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def go(root):
            if not root:
                return 0
            l = go(root.left)
            r = go(root.right)

            if not root.left and not root.right or root.left and root.right:
                return min(l, r) + 1

            return max(l, r) + 1


        return go(root)
