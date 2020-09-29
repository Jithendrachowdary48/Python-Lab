#Binary Search by User Input

def BinarySearch(a,low,high,search):
    if high>=low:
        mid=(low+high)//2
        if a[mid]==search:
            return mid
        elif a[mid]>search:
            return BinarySearch(a,low,mid-1,search)
        else:
            return BinarySearch(a,mid+1,high,search)    
    else:
        return -1
l=list(map(int,input("Enter array ").split()))
find=int(input("Enter element to find "))
pos=BinarySearch(l,0,len(l)-1,find)
if pos==-1:
    print("element not found")
else:
    print("Element",find,"found at",pos,"index")
