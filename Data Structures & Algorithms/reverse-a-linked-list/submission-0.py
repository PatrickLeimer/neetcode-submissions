# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Hi again party people
        I think the most optimal here is O(n) bc we don't have the tail pointer
        So iterate through the pointers, then once we find tail here the logic
        1 -> 2 -> 3 -> 4 -> 5 -> 6
        head pointer becomes tail 
        temp stores head pointer?
        then we move onto next pointer and assign the head pointer to next of current
        assign curr pointer of 2 to temp 
        and so on until the end
        so the new head is 6

        Reflection:
        Pretty straight forward, nothing much to think other than the swap logic
        for some reason I made a mistake in the while loop and that took me a while to debug
        '''

        #base case
        if head is None:
            return head

        # 1 2 3
        current = head # 2
        prev = None # 1

        while current is not None:
            temp = current.next 

            # 1 points to nothing 
            # current is pointing at 2 
            # prev is 1
            # So know, point 2.next to prev
            # set prev to 2/current
            # set current to temp

            # second run 
            # current is 3, prev is 2, temp is None
            # assign current next to 2, prev = current which is 3, and current gets none/temp 

            current.next = prev # head becomes tail
            prev = current 
            current = temp 

        return prev
        