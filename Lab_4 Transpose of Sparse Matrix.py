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

def trans(arr):
    res = []
    for i in arr:
        res.append([i[1],i[0],i[2]])
    res.sort()
    return res

def print_martix(arr):
    if arr==[]: print("Empty Matrix")
    for i in arr:
        print(*i)
arr = []

#Inputs
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))
for i in range(r):
    dup = list(map(int,input().split()))
    arr.append(dup)

print("The Original Matrix")
print_martix(arr)

print()

#Sparse matrix
sparse = sparse_matrix(arr)
print("The Sparse Matrix")
print_martix(sparse)

#Transpose of a sparse matrix
transpose = trans(sparse)
print("The Transpose of the Sparse Matrix")
print_martix(transpose)
