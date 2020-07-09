# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # if no root, width is 0
        if not root:
            return 0
        
        # this is our default if we just have a root node
        max_width = 1
        
        # do bfs to go level by level
        queue = deque()
        queue.append((root, 1)) # queue holds node and its position

        while queue:
            
            #figure out the length in that level
            level_size = len(queue)
            
            # max width is the length from pos of right most node minus pos of left most node (plus 1)
            max_width = max(queue[-1][1] - queue[0][-1] + 1, max_width)
            
            # pop everything from that level from queue and add new nodes from lower level, with pos
            while level_size:
                node, pos = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*pos)) #node left is pos of parent * 2
                if node.right:
                    queue.append((node.right, 2*pos + 1)) # node right is pos of parent * 2 + 1
                level_size -= 1
           
        return max_width
