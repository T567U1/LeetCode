# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def go(root, s):
            if not root:
                return s
            s += str(root.val)
            return go(root.next, s)

        add1 = go(l1, '')
        add2 = go(l2, '')
        add_ = str(int(add1) + int(add2))

        ans = ListNode(add_[0])
        temp = ans
        for i in add_[1:]:
            temp.next = ListNode(i)
            temp = temp.next

        return ans
