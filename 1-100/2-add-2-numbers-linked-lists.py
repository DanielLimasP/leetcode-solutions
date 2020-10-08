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

# It takes for input the first node of two lists
def addTwoNumbers(l1, l2):
    strL1, strL2 = '', ''
    while l1:
        strL1 += str(l1.val)
        l1 = l1.next
    while l2:
        strL2 += str(l2.val)
        l2 = l2.next
    intL1 = int(strL1[::-1])
    intL2 = int(strL2[::-1])
    return list(map(int, str(intL1 + intL2)[::-1]))

def testCode():
    l1 = SimpleLinkedList()
    l2 = SimpleLinkedList()
    numberList_1 = [2, 4, 3]
    numberList_2 = [5, 6, 4]
    l1.createList(numberList_1)
    l2.createList(numberList_2)
    # List 1
    #l1.iterateList(l1.first)
    # List 2
    #l2.iterateList(l2.first)
    
    # AddTwoNumbers Test
    print(addTwoNumbers(l1.first, l2.first))

testCode()