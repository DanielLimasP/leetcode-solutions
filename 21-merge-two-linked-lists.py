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
    def mergelists(self, otherList):
        aux = self.first
        aux2 = otherList.first

        while aux != None:
            if aux == None:
                break 
            print(aux.val)
            aux = aux.next

            

if __name__ == "__main__":
    testList = SimpleLinkedList()
    testList.createList([1, 2, 3, 4, 5])

    otherList = SimpleLinkedList()
    otherList.createList([1, 2, 3, 4, 5])
    #testList.iterateList(testList.first)

    testList.mergelists(otherList)
