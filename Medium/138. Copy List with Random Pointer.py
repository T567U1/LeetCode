"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ans = Node(0)
        n = ans
        index_ = []
        temp = head

        while temp:
            n.next = Node(temp.val)
            index_ += temp,
            temp = temp.next
            n = n.next

        n = ans.next
        temp = head

        while temp:
            if temp.random:
                i = 0
                x = ans
                while i != index_.index(temp.random) + 1:
                    x = x.next
                    i += 1

                n.random = x

            n = n.next
            temp = temp.next

        return ans.next
    # clone is a thing.......
    def copyRandomList(self, head: 'Node') -> 'Node':

        clone_prehead = Node(0) # To keep track of the new list head and to avoid having 2 cases (cloning the head node and internal nodes)

		# 1. Clone Values and Next pointers
        clone = clone_prehead
        while head:
            clone.next = Node(head.val, None, head.random)
            clone = clone.next

            head.next, head = clone, head.next

		# 2. Clone Random pointers
        clone = clone_prehead.next
        while clone:
            if clone.random:
                clone.random = clone.random.next

            clone = clone.next

        return clone_prehead.next
