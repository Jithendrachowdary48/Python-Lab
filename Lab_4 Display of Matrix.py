def displaying_sparse_matrix(a):
    sp1 = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != 0:
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(a[i][j])
                sp1.append(temp)

    print('''The Sparse Matrix Representation :
    Row\tCol\tValue\t''')
    for i in sp1:
        for x in i:
            print(x, end=' \t ')
        print()
n = int(input('Enter the value of N in NxN Matrix : '))
a = []
for i in range(n):
    x = []
    print(f'Enter the values in {i}th row : ')
    for j in range(n):
        x.append(int(input()))
    a.append(x)
displaying_sparse_matrix(a)
