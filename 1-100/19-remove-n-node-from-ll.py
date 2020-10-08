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

    # This function is the solution to problem 19
    def removeNfromLast(self, n):
        aux = ListNode(0)
        aux.next = self.first
        length = 0
        f = self.first
        while f != None:
            length += 1
            f = f.next
        
        length -= n
        f = aux

        while length > 0:
            length -= 1
            f = f.next
        
        f.next = f.next.next
        return aux.next


if __name__ == "__main__":
    testList = SimpleLinkedList()
    testList.createList([1, 2, 3, 4, 5])
    testList.iterateList(testList.removeNfromLast(2))