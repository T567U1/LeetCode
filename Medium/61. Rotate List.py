import heapq as h
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        l, temp = 0, head
        while temp:
            l += 1
            temp = temp.next

        k = k % l

        while k:
            temp = head
            while temp.next.next:
                temp = temp.next
            temp.next.next = head
            head = temp.next
            temp.next = None
            k -= 1

        return head
    
