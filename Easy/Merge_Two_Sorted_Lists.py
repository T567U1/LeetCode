class Solution(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """



l1 = Solution(1)
l1.next = Solution(2)
l1.next.next = Solution(4)
l2 = Solution(1)
l2.next = Solution(3)
l2.next.next = Solution(4)
