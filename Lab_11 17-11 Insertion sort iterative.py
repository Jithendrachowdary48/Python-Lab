#Program on Insertion sort
#Function performing sort
def insertionSort(array):
    for x in range(1, len(array)):
        key = array[x]
        j = x - 1       
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
l=[]
#Inputs
n = int(input("Enter size :"))
for x in range(n):
   l.append(int(input("Enter Elements :")))
print("list :",l)
insertionSort(l)
#Outputs
print("Sorted Array in Ascending Order :")
print("list :",l)
