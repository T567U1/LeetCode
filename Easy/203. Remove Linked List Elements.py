# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        '''if not head:
            return head
        ans = ListNode(None)
        temp = ans
        while head:
            print(head.val)
            if head.val == val:
                head = head.next
            else:
                temp.next = ListNode(head.val)
                temp = temp.next
                head = head.next

        return head'''
        # optomized
        pre = ListNode(None)
        pre.next = head
        cur = pre

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return pre.next

c = Solution()
print(c.removeElements(, 6))
