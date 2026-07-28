# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1=list1
        head2=list2
        head_res=ListNode()
        e=head_res
        while head1!=None and head2!=None:
            if head1.val<=head2.val:
                e.next=head1
                e=e.next
                head1=head1.next
            else:
                e.next=head2
                e=e.next
                head2=head2.next
        while head1!=None:
            e.next=head1
            e=e.next
            head1=head1.next
        while head2!=None:
            e.next=head2
            e=e.next
            head2=head2.next
        return head_res.next

                
