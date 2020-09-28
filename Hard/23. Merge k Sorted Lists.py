# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        a = []
        for arr in lists:
            while arr:
                a += arr.val,
                arr = arr.next

        if not a:
            return None

        a.sort()
        ans = ListNode(a.pop())

        while a:
            ans = ListNode(a.pop(), ans)

        return ans
