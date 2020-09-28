class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []
        def go(root):
            if not root:
                return
            self.ans += root.val,
            return go(root.left), go(root.right)

        go(root)
        return self.ans
