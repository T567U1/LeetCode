# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arr = []
        def go(root):
            if not root:
                return
            self.arr += root.val,
            go(root.left)
            go(root.right)

        go(root)
        self.arr.sort(reverse = True)
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.arr.pop()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.arr)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
