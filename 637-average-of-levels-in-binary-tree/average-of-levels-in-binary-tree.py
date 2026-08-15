# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q,res=deque([root]),[]
        while q:
            level=[node.val for node in q]
            res.append(sum(level)/len(level)) 
            for _ in range(len(q)):
                node = q.popleft() 
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
        return res      