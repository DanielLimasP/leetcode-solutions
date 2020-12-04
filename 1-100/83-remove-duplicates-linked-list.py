class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    dummy = prev = ListNode(0)
    dummy.next = head
    
    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            prev.next = head
        else:
            head = head.next
            prev = prev.next
    
    return dummy.next
            