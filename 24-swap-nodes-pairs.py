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

    # Solution for problem 24
    # https://codesays.com/2014/solution-to-swap-nodes-in-pairs-by-leetcode/
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head

        newHead = head.next

        current = head
        previous = None

        while current != None and current.next != None:
            if previous != None:
                previous.next = current.next
            # 1
            previous = current
            # 2
            temp = current.next.next
            # 3
            current.next.next = current
            # 4
            current.next = temp
            # 5
            current = current.next
        return newHead

if __name__ == "__main__":
    testList = SimpleLinkedList()
    testList.createList([1, 3, 5, 7, 9])
    testList.iterateList(testList.first)



