#Linear Search by User input
#Inputs
print("Enter an array")
l=list(map(int,input().split()))
find=int(input("Enter a digit to find "))
def linearsearch(a,search):
    for i in range(len(a)):
        if a[i]==find:
            return i
pos=linearsearch(l,find)
if pos==None:
    print("Element Not Found")
else:
    print(find,"found at",pos,"index")
