# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def go(pre, root, n, i = 0):
            if not head:
                return
            p = get_index(root)
            if p == n:
                if not i:
                    return 0
                pre.next = root.next
                return i
            return go(root, root.next, n, i + 1)

        def get_index(root, a = 0):
            if not root:
                return a
            a += 1
            return get_index(root.next, a)

        ans = go(head, head, n)

        return head if ans else head.next
            
