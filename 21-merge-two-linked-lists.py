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

    # This function is the solution to problem 21
    # https://www.youtube.com/watch?v=GfRQvf7MB3k
    def mergelists(self, otherList):
        l1 = self.first
        l2 = otherList.first
        curr = None

        # First comparison to see where the dummy head will begin
        if l1.val <= l2.val:
            curr = l1
            l1 = l1.next
        else:
            curr = l2
            l2 = l2.next

        dummy = curr

        # Iterate through both lists making comparisons and rewiring nodes
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                curr = l1
                l1 = curr.next
            else:
                curr.next = l2
                curr = l2
                l2 = curr.next
            
        if not l1:
            curr.next = l1
        if not l2:
            curr.next = l2

        return dummy

if __name__ == "__main__":
    testList = SimpleLinkedList()
    testList.createList([1, 3, 5, 7, 9])

    otherList = SimpleLinkedList()
    otherList.createList([2, 4, 6, 8, 10])
    #testList.iterateList(testList.first)

    testList.iterateList(testList.mergelists(otherList))
