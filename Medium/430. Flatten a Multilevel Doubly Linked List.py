class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        self.nums = []
        def go(root):
            if not root:
                return
            if root.child:
                self.nums.append(root.val)
                go(root.child)
            else:
                self.nums.append(root.val)
            return go(root.next)
        go(head)
        ans = Node(self.nums[0])
        temp = ans
        for i in self.nums[1:]:
            temp.next = Node(i)
            temp.next.prev = temp
            temp = temp.next

        return ans
