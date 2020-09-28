# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        self.catch = []
        def go(head, prev = 0):
            if not head:
                return
            self.catch += head.val,
            return go(head.next, head)

        go(head)
        ans = ListNode()
        t = ans

        for i in sorted(set(self.catch)):
            if self.catch.count(i) > 1:
                continue
            t.next = ListNode(i)
            t = t.next

        return ans.next
