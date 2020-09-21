# Function to represent the Sparse Matrix
def sparse_matrix(arr):
    sp = []
    r = len(arr)
    c = len(arr[0])
    for i in range(r):
        for j in range(c):
            if arr[i][j]!=0:
                sp.append([i,j,arr[i][j]])
    return sp

# Function to add two sparse matrices
def add(arr1,arr2):
    res = [] 
    l1 = len(arr1)
    l2 = len(arr2)
    if l1==0 : res = arr2
    if l2==0 : res = arr1
    i = 0
    j = 0
    while l1>0 and l2>0:
        if arr1[i][0]==arr2[j][0] and arr1[i][1]==arr2[j][1]:
            res.append([arr1[i][0],arr1[i][1],arr1[i][2]+arr2[j][2]])
            i += 1
            j += 1
        else:
            m = min(arr1[i],arr2[j])
            res.append(m)
            if m==arr1[i]:
                i += 1
            else:
                j += 1
        if i>=l1:
            for x in range(j,l2):
                res.append(arr2[x])
            break
        if j>=l2:
            for x in range(i,l1):
                res.append(arr1[x])
            break
    return res

def print_martix(arr):
    if arr==[]: print('EMPTY MATRIX')
    for i in arr:
        print(*i)

def input_matrix(r):
    arr = []
    i = 0
    while i<r:
        dup = list(map(int,input().split()))
        arr.append(dup)
        i += 1
    return arr


#Inputs
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))
print("Enter Martix 1")
arr1 = input_matrix(r)
print("Enter Martix 2")
arr2 = input_matrix(r)

#Original Matrices
print("The Original Matrices are")
print("Matrix 1")
print_martix(arr1)
print("Matrix 2")
print_martix(arr2)
print()

#Printing Sparse Matrices
print("The Sparse Matrices are")
sp1 = sparse_matrix(arr1)
sp2 = sparse_matrix(arr2)
print("Sparse Matrix 1")
print_martix(sp1)
print("Sparse Matrix 2")
print_martix(sp2)
print()

#Result
print("Addition of 2 Sparse Matrices")
result = add(sp1,sp2)
print_martix(result)
