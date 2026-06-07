# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1,p2=headA,headB
        c=0
        while True:
            if p1==p2:return p1
            p1=p1.next
            p2=p2.next
            if not p2:
                p2=headA
                c+=1
            if not p1:
                p1=headB
            if c>1:return None
        