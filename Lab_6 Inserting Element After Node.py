class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def insert_at_position(self,key,data):
        new_node = Node(data)
        cur = self.head
        while cur:
            nxt = cur.next
            if cur.data == key:
                cur.next = new_node
                new_node.next = nxt
                return
            cur = cur.next
        print("Node not found")
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
l=LinkedList()
n=int(input("Enter how many num to be added :"))
for i in range(n):
    data=int(input("enter data :"))
    l.append(data)
l.print_list()
k=int(input("Enter the element :"))
i=int(input("Enter the element to be inserted after node :"))
l.insert_at_position(i,k)
l.print_list()
