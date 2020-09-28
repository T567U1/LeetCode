class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.ans = {}
        l = 0
        def avg(root, l):
            if not root:
                return
            if l in self.ans:
                self.ans[l].append(root.val)
            else:
                self.ans[l] = [root.val]

            return avg(root.right, l + 1), avg(root.left, l + 1)

        avg(root, l)
        self.ans[0] = [root.val]
        return [sum(self.ans[i]) / len(self.ans[i]) for i in self.ans]
