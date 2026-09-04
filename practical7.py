# 1. Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


print("Singly Linked List:")
l1 = LinkedList()

l1.insert(10)
l1.insert(20)
l1.insert(30)

l1.display()


# 2. Doubly Linked List Node

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


print("\nDoubly Linked List Node:")
node = DoublyNode(10)

print("Data:", node.data)
print("Previous:", node.prev)
print("Next:", node.next)


# 3. Circular Linked List

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = CircularNode(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


print("\nCircular Linked List:")
cll = CircularLinkedList()

cll.insert(5)
cll.insert(10)
cll.insert(15)

cll.display()
