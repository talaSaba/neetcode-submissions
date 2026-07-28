# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # 1. Find the middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # slow is the final node of the first half
        second = slow.next
        slow.next = None

        # 2. Reverse the second half
        previous = None
        current = second

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        second = previous
        first = head

        # 3. Merge alternately
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next 



        
