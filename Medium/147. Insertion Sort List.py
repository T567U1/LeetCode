# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        def go(head, a = []):
            if not head:
                return a
            a += head.val,
            return go(head.next, a)
        a = go(head)
        a.sort()
        ans = ListNode(a.pop())
        while a:
            ans = ListNode(a.pop(), ans)

        return ans
