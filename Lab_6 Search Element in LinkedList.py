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
    def search(self,key):
        temp=self.head
        while temp:
            if temp.data==key:
                print("element found")
                return
            temp=temp.next
        print("Element not found")
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
l=LinkedList()
n=int(input("Enter how many num to be added :"))
for i in range(n):
    data=int(input("Enter data :"))
    l.append(data)
l.print_list()
k=int(input("Enter search element :"))
l.search(k)
