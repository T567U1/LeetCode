# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        self.ans = []
        self.k = k
        def go(k, head, arr = []):
            if not head:
                if not k:
                    self.ans.extend(arr[::-1])
                else:
                    self.ans.extend(arr)
                return
            if not k:
                self.ans.extend(arr[::-1])
                k = self.k
                arr = []

            arr += head.val,

            go(k - 1, head.next, arr)

        go(k, head)
        ans = ListNode(self.ans.pop())

        while self.ans:
            ans = ListNode(self.ans.pop(), ans)

        return ans
