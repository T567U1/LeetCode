class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, l2: ListNode) -> ListNode:
        def go(root, a = None):
            if not root.next:
                a = root
                return a
            return go(root.next, a)

        def go1(root, a, b, prev = None):
            if not root:
                return
            if not a:
                prev.next = self.l2
            if b == -1:
                self.endL2.next = root

            go1(root.next, a - 1, b - 1, root)

        self.endL2 = go(l2)
        self.l2 = l2
        go1(list1, a, b)

        return list1
