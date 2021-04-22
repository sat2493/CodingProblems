# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        print("here")
        # Check for head, and keep employing this for case of 2 - 2 - 2 - ...
        print(head.val)
        #
        while head.val == val and head:
            # Move the head forward
            head = head.next
            
        # Empty list
        if head == None:
            return head
          
        return head
        

#        # Set up the incrementer
#        curr = head
#        # Traverse the entire linked list
#        while curr != None:
#            # Check the next node's value
#            # Case val == Node.val
#            if curr.next.val == val:
#                # Remove accordingly by: 
#                # Changing the status of current node from grandparent to parent
#                temp = curr.next
#                curr.next = curr.next.next
#                # Removing the former rightful parent from memory
#                del temp
#                
#            # Move on to the next node
#            curr = curr.next  
