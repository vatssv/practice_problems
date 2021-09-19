"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        queue = []
        if not(root):
            return
        first = root.val
        current_level, current_level_nodes = 0, 0
        def bfs(root: 'Node'):
            if root == None:
                return
            queue.pop(0)
            nonlocal current_level_nodes
            current_level_nodes += 1
            queue.append(root.left)
            queue.append(root.right)
            nonlocal current_level
            if current_level_nodes < 2 ** current_level:
                root.next = queue[0]
            else:
                current_level_nodes = 0
                current_level += 1
                root.next = None
            bfs(queue[0])
            return
        queue.append(root)
        bfs(root)
        return root