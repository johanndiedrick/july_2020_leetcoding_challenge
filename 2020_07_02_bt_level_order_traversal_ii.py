# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        
        if not root:
            return result
        
        # try bfs
        queue = deque()
        
        #push in root node
        queue.append(root)
        
        while queue:
            level_size = len(queue)
            
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)

        result.reverse()
        return result
