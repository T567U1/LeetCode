# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        v = []
        t = head
        while t:
            v += t.val,
            t = t.next

        v.pop(0)
        head.next = None
        t = head
        f = 1

        while v:
            if f:
                t.next = ListNode(v.pop())
                f = 0
            else:
                t.next = ListNode(v.pop(0))
                f = 1
            t = t.next
