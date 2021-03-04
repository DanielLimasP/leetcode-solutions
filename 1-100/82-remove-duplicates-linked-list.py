class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates_linked_list(head):
    dummy = previous = ListNode(0)
    dummy.next = head
    
    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            previous.next = head
        else:
            previous = previous.next
            head = head.next
    
    return dummy.next

# No need to run this one...