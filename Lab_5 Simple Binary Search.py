a=[1,2,3,4,5,6,7,8,9]
n=4
low=0
high=len(a)
mid=(low + high) // 2
if (a[mid] < n):
    for i in range(mid,high):
        if (a[i] == n):
            print(n," is Found in ",i)
elif (a[mid] == n):
    print(n," is Found in ",mid)
else:
    for i in range(low,mid):
        if (a[i] == n):
            print(n," is Found in ",i)
