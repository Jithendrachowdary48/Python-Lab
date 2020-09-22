def LinearSearch(x,n,a):
    for i in range(0,n):
        if (a[i] == x):
            print(x," is present in index ",i)
            break
        
a = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
        value = int(input())
        a.append(value)
x = int(input("Enter Search Element : "))
LinearSearch(x,n,a)
