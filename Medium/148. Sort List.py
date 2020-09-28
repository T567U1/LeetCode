# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        self.ans = None
        def go(head, arr = []):
            if not head:
                arr.sort()
                ans = ListNode(arr.pop())
                while arr:
                    ans = ListNode(arr.pop(), ans)
                self.ans = ans
                return

            arr += head.val,
            go(head.next, arr)

        go(head)
        return self.ans
            
