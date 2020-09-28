# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def get_nodes(root):
            if root is None:
                return
            return get_nodes(root.right), get_nodes(root.left), ans.append(root.val)

        def deg_right_tree(ans):
            ans_ = TreeNode(ans[0])
            temp = ans_
            for i in range(1, len(ans)):
                temp.right = TreeNode(ans[i])
                temp = temp.right
            return ans_

        get_nodes(root)
        return deg_right_tree(sorted(ans))
        
