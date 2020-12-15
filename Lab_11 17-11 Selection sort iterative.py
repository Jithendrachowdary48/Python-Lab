#Program on Selection Sort
#Function performing sort
def selectionSort(array, size):
    for x in range(size):
        min = x
        for i in range(x + 1, size):
            if array[i] < array[min]:
                min = i
        (array[x], array[min]) = (array[min], array[x])
l=[]
#Inputs
n=int(input("Enter size :"))
for i in range(n):
    l.append(int(input("Enter Elements :")))
#Outputs
print("list :",l)
selectionSort(l,n)
print("List :",l)
