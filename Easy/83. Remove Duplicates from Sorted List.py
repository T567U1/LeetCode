# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return ListNode()
        seen = [head.val]
        s = ListNode(head.val)
        t = s
        while head:
            if head.val not in seen:
                seen.append(head.val)
                t.next = ListNode(head.val)
                t = t.next
            head = head.next
        return s
