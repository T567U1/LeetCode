# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.ans = []
        def get_e(root):
            if not root:
                return
            self.ans.append(root.val)
            return get_e(root.left), get_e(root.right)

        get_e(root1)
        get_e(root2)

        return sorted(self.ans)
