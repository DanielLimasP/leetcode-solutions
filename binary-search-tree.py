#Daily Coding Problem 3: 

# Given the root to a binary tree, implement serialize(root), which serializes 
# the tree into a string, and deserialize(s), which deserializes the string 
# back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def empty(self):
        return self.root is None

    def __insert(self, value):
        new_node = Node(value, None)
        if self.empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *values):
        for value in values:
            self.__insert(value)
        return self            
                    
    def search(self, value):
        if self.empty():
            raise IndexError("Warning, tree is empty")
        else:
            node = self.root
            while node is not None and node.value is not value:
                node = node.left if value < node.value else node.right
            return node

    def inorder_traverse(self, node):
        if node is not None:
            self.inorder_traverse(node.left)
            print(node.value)
            self.inorder_traverse(node.right)
    
    def preorder_traverse(self, node):
        if node is not None:
            print(node.value)
            self.inorder_traverse(node.left)
            self.inorder_traverse(node.right)
            
def binary_search_tree():
    testList = (8, 3, 6, 1, 10, 14, 13, 4, 7)
    t = BinaryTree()
    for i in testList:
        t.insert(i)

    print(t)
    if t.search(9) is not None:
        print('Value has been found!')
    else:
        print('The value does not exist')

    #t.inorder_traverse(t.root)
    print(t.inorder_traverse(t.root))

binary_search_tree()