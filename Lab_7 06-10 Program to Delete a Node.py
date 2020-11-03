# Python program to delete a node from linked list    
class Node:
    def __init__(self, data):  
        self.data = data  
        self.next = None
  
class LinkedList:   
    def __init__(self):  
        self.head = None
    def push(self, new_data):  
        new_node = Node(new_data)  
        new_node.next = self.head  
        self.head = new_node    
    # delete the first occurence of key in linked list  
    def deleteNode(self, key):  
        temp = self.head  
  # If head node itself holds the key to be deleted  
        if (temp is not None):  
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return
  # Search for the key to be deleted, keep track of the   
        while(temp is not None):  
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
  
        # if key was not present in linked list  
        if(temp == None):  
            return
  
        # Unlink the node from linked list  
        prev.next = temp.next
  
        temp = None
  
  
    # Utility function to print the linked LinkedList  
    def printList(self):  
        temp = self.head  
        while(temp):  
            print (" %d" %(temp.data)),  
            temp = temp.next
  
 
llist = LinkedList()  
llist.push(4)  
llist.push(1)  
llist.push(6)  
llist.push(9)  
  
print ("Created Linked List: ") 
llist.printList()  
llist.deleteNode(4)  
print ("\nLinked List after Deletion:") 
llist.printList()
