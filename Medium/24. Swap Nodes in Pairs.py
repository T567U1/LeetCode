# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        def go(root, ans = []):
            if not root:
                return ans
            if root.next:
                ans += root.next.val, root.val,
            else:
                ans += root.val,
                return ans
            return go(root.next.next)

        ans_ = go(head)
        temp = ListNode(ans_.pop())

        while ans_:
            ans = ListNode(ans_.pop())
            ans.next = temp
            temp = ans

        return ans
