# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,mn,mx):
        if not root:return True
        if root.val>mx or root.val<mn:return False
        cl=self.check(root.left,mn,root.val-1)
        cr=self.check(root.right,root.val+1,mx)
        return cl and cr
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root,float('-inf'),float('inf'))
        