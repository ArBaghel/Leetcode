# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:return head
        l,last=0,head
        while last.next:
            last=last.next
            l +=1
        l+=1
        k=k%l
        if k==0:return head
        cur=head
        for i in range(l-k-1):
            cur=cur.next
        last.next=head
        head=cur.next
        cur.next=None
        return head

        