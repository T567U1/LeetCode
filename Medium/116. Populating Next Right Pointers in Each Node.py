"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.level = {}
        def go(root, level = 0):
            if not root:
                return
            if level in self.level:
                self.level[level].next = root
                self.level[level] = root
            else:
                self.level[level] = root

            go(root.left, level + 1)
            go(root.right, level + 1)

        go(root)
        return root
