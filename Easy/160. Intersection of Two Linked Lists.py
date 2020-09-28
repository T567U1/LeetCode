class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dic = {}
        while headA:
            dic[id(headA)] = headA.val
            headA = headA.next

        while headB:
            if id(headB) in dic.keys():
                 return headB
            headB = headB.next

        return None
