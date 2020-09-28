class Node:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = Node

c = Node(2)
c.left = Node(3)
c.right = Node(2)
c.right.left = Node(10)
