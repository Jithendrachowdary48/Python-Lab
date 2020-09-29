def BinarySearchAscending(a,low,high,search):
    if high>=low:
        mid=(low+high)//2
        if a[mid]==search:
            return mid
        elif a[mid]>search:
            return BinarySearchAscending(a,low,mid-1,search)
        else:
            return BinarySearchAscending(a,mid+1,high,search)    
    else:
        return -1
def BinarySearchDescending(a,low,high,search):
    if high>=low:
        mid=(low+high)//2
        if a[mid]==search:
            return mid
        elif a[mid]<search:
            return BinarySearchDescending(a,low,mid-1,search)
        else:
            return BinarySearchDescending(a,mid+1,high,search)    
    else:
        return -1
#Taking input of a list in one line
l=list(map(int,input("Enter array ").split()))

#checking whether given list is empty or not
if len(l)>0:
    #This if finds whether given list is sorted in Ascending order or not
    if l==sorted(l):
        find=int(input("Enter element to find "))
        #Now this calls the function needed when list is in ascending order
        pos=BinarySearchAscending(l,0,len(l)-1,find)
        if pos==-1:
            print("element not found")
        else:
            print("Element",find,"found at",pos,"index")
    #This elif finds whether given list is sorted in Descending order or not
    elif l==sorted(l,reverse=True):
        find=int(input("Enter element to find "))
        #Now this calls the function needed when list is in descending order
        pos=BinarySearchDescending(l,0,len(l)-1,find)
        if pos==-1:
            print("element not found")
        else:
            print("Element",find,"found at",pos,"index")
    #If the list is not sorted then this else gets executed
    else:
        print("Binary search not possible beacause given list is not sorted")
else:
    print("list is empty")
