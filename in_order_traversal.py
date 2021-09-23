# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return
        if root.left == None and root.right == None:
            return [root.val]
        res = []
        def in_order_traversal(root):
            if root == None:
                return
            else:
                if root.left != None:
                    r = in_order_traversal(root.left)
                    if r != None:
                        res.append(r)
                res.append(root.val)
                if root.right != None:
                    r = in_order_traversal(root.right)
                    if r != None:
                        res.append(r)
                return
        in_order_traversal(root)
        return res