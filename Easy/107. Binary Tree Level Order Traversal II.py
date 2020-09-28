class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        level = 0

        def get_val(level, root):
            if root:
                if len(res) < level:
                    res.append([root.val])
                else:
                    res[level - 1].append(root.val)

                get_val(level + 1, root.left)
                get_val(level + 1, root.right)

        get_val(1, root)

        return res[::-1]
