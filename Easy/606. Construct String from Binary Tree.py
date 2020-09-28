class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def go(root):
            if not root:
                return ''

            if not root.left and not root.right:
                return str(root.val)

            if not root.right:
                return f'{root.val}({go(root.left)})'

            return f'{root.val}({go(root.left)})({go(root.right)})'

        return go(t)
