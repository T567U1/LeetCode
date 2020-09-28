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
        self.rows = {}
        #node and depth level
        def go(root, row):
            if not root:
                return
            #if row just link it to root and replace row
            if row in self.rows:
                self.rows[row].next = root
                self.rows[row] = root
            else:
                self.rows[row] = root
            return go(root.left, row + 1), go(root.right, row + 1)
        go(root, 0)
        return root
