def anti_diagonal(rows,columns,matrix):
    for x in range(rows-1):
        i=0
        j=x
        while i<rows:
            if 0<=j<columns:
                print(matrix[i][j],end=" ")
            else:
                print("0",end=" ")
            i+=1
            j-=1
        print()

    for y in range(columns):
        i=y
        j=columns-1
        while j>=0:
            if 0<=i<rows:
                print(matrix[i][j], end=" ")
            else:
                print("0", end=" ")
            i += 1
            j -= 1
        print()


matrix=[]
rows=int(input("Enter number of rows : "))
columns=int(input("Enter number of columns : "))
for i in range(rows):
    matrix.append(list(map(int,input().split())))
anti_diagonal(rows,columns,matrix)