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
        head.next=None# very important --\. severe the head and then 
        while prev.next != None:
            temp=prev.next
            prev.next=neext
            neext=prev
            prev=temp
        prev.next = neext #the last one just connect the prev.next to neext
        return prev


        
        