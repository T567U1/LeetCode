class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.ans, l = 0, 1
        def go(root, x):
            if not root:
                return
            self.ans = max(x, self.ans)
            for i in root.children:
                go(i, x + 1)
        go(root, l)
        return self.ans
