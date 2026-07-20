# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #h=head
        if head==None:
            return 
        if head.next==None:
            return head
        prev=head.next
        
        neext=head
        head.next=None
        while prev.next != None:
            temp=prev.next
            prev.next=neext
            neext=prev
            prev=temp
        prev.next = neext 
        return prev


        
        