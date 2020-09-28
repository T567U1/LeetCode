# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head

        def go(head, a = []):
            if not head:
                return a
            a += head.val,
            return go(head.next)

        def ma(arr, root):
            if not arr:
                return root
            t = ListNode(arr.pop())
            t.next = root
            root = t
            return ma(arr, root)

        a = go(head)
        a = a[:m - 1] + a[m - 1: n][::-1] + a[n:]
        root = ListNode(a.pop())
        root = ma(a, root)

        return root
