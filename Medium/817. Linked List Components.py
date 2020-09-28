# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        temp = []
        ans = []
        while head:
            if head.val not in G:
                if temp:
                    ans.extend([temp])
                temp.clear()
            else:
                temp.append(head.val)
            head = head.next
        if temp:
            ans.extend([temp])
        return len(ans)
