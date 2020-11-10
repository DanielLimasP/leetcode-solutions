# Linked list definition somewhere inside a problem
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def rotate_by_k(k, head):
    if not head:
        return None
    last_node = head
    length = 1

    while last_node.next:
        last_node = last_node.next
        length += 1

    k = k % length

    last_node.next = head

    temp = head

    for _ in range(length - k - 1):
        temp = temp.next

    ans = temp.next
    temp.next = None

    return ans
