#Identify the biggest and smallest key in a linked list containing integers.
class Node: 
  
    def __init__(self): 
        self.data = None
        self.next = None
  head = None
def largestElement(head):   
    max = -32767 
    while (head != None):   
        if (max < head.data) : 
            max = head.data  
        head = head.next
      
    return max 
def smallestElement(head):   
    min = 32767 
    while (head != None) :  
        if (min > head.data) : 
            min = head.data  
        head = head.next
      return min
def push( data) : 
  
    global head  
    newNode = Node()   
    newNode.data = data    
    newNode.next = (head)  
    (head) = newNode    
push(75)  
push(34)  
push(53)  
push(22)  
push(30)      
print("Maximum element in linked list: ",end="")   
print(largestElement(head))  
print("Minimum element in linked list: ",end="")   
print(smallestElement(head),end="")  
