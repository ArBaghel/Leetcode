# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], t: int) -> Optional[TreeNode]:
        if not root:return None
        cur=root
        while cur:
            if cur.val==t:return cur
            if t<cur.val:
                cur=cur.left
            elif t>cur.val:
                cur=cur.right
        return None
        