# Divide and conquer approach
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class SimpleLinkedList:
    def __init__(self, first=None, last=None):
        self.first = first

    def isEmpty(self):
        if self.first is None:
            return True
        else: 
            return False

    def insertNode(self, node):
        if self.isEmpty():
            self.first = node
            self.last = node
        elif self.last.next is None:
            self.last.next = node
            self.last = node

    def iterateList(self, listNode):
        if listNode.next == None:
            print(listNode.val)
            return None
        else:
            print(listNode.val)
            self.iterateList(listNode.next)
    
    def createList(self, numList):
        for i in numList:
            node = ListNode(i)
            self.insertNode(node)

    # TODO: Study this solution
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
            dummy = curr = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next
        
        if lists == None:
            return None
        
        N = len(lists)
        mid = N // 2
        
        if N == 1:
            return lists[0]
        
        top, bottom = None, None
        if mid > 0:
            top = self.mergeKLists(lists[:mid])
        if mid <= N-1:
            bottom = self.mergeKLists(lists[mid:])
        
        # merge two lists
        return mergeTwoLists(top, bottom)

if __name__ == "__main__":
    testList = SimpleLinkedList()
    testList.createList([1, 3, 5, 7, 9])

    otherList = SimpleLinkedList()
    otherList.createList([2, 4, 6, 8, 10])
    #testList.iterateList(testList.first)



