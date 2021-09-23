# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 == None and root2 == None:
            return
        r = TreeNode(0)
        def multi_dfs(root, root1, root2):
            if root1 == None and root2 == None:
                return
            else:
                l1, l2 = None if not root1 else root1.left, None if not root2 else root2.left
                r1, r2 = None if not root1 else root1.right, None if not root2 else root2.right
                r1_val, r2_val = 0 if not root1 else root1.val, 0 if not root2 else root2.val
                root.val = r1_val + r2_val
                root.left = TreeNode(0) if l1 or l2 else None
                root.right = TreeNode(0) if r1 or r2 else None
                multi_dfs(root.left, l1, l2)
                multi_dfs(root.right, r1, r2)
                return
        multi_dfs(r, root1, root2)
        return r