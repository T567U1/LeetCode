# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        self.x, self.y = [], []
        self.limit = x

        def go(head, x, flag = False):
            if not head:
                return
            if not flag and head.val >= x:
                flag = True
            if flag:
                if head.val < self.limit:
                    self.x += head.val,
                else:
                    self.y += head.val,
            else:
                self.x += head.val,
            return go(head.next, x, flag)

        go(head, x - 1)

        a = self.x + self.y
        ans = ListNode(a.pop())

        while a:
            t = ListNode(a.pop())
            t.next = ans
            ans = t

        return ans
