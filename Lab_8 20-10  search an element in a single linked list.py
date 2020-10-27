#  A.pavan kumar - 121910313047
# Program to search an element in a singly linked list

# Defining the Node class
class Node:
    def __init__(self,data): 
        self.data = data
        self.prev = None
        self.next = None

# Definind the Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to append new nodes
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    # Method to search Node in a Linked List
    def search(self,key):
        cur = self.head
        while cur:
            if cur.data==key: return True
            cur = cur.next
        return False


    

dll = DoublyLinkedList()
n = int(input("Enter the size of the linked list : "))
print("Enter the elements of the linked list")
for i in range(n):
    dll.append(input())

k = input("Enter the element to search : ")
ans = dll.search(k)
if ans: print("Element is present")
else: print("Element is not present")
