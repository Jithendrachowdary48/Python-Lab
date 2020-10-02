class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:

    def __init__(self):
        self.head=None
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
l=LinkedList()
l.head=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)
l.head.next=second
second.next=third
third.next=fourth
l.print_list()
