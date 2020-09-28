# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        while l1 or l2:
            if l1:
                num1 = str(l1.val) + num1
                l1 = l1.next
            if l2:
                num2 = str(l2.val) + num2
                l2 = l2.next

        ans = str(int(num1) + int(num2))
        ans_list = ListNode(None)
        temp = ans_list
        for num in ans[::-1]:
            temp.next = ListNode(int(num))
            temp = temp.next
        return ans_list.next
