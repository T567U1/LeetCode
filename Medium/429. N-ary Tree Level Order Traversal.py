"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.ans = {}
        def go(root, level):
            if not root:
                return
            if level in self.ans:
                self.ans[level].extend([root.val])
            else:
                self.ans[level] = [root.val]
            for i in root.children:
                go(i, level + 1)

        go(root, 0)

        return list(self.ans.values())
