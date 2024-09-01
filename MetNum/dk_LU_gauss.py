A = [[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]]

def show(matrix):
    n= len(matrix)
    for row in range(n):
        for col in range(n):
            print("%.2f" % matrix[row][col], end="\t")
        print("")

show(A)

def decompos(A):
    n= len(A)
    L= [[0 for row in range(n)] for col in range(n)]
    U= [[0 for row in range(n)] for col in range(n)]

    for p in range(n):
        for j in range(p,n):
            sum = 0
            for k in range(p):
                sum=sum+L[p][k]*U[k][j]
                U[p][j]=A[p][j] - sum

        q = p
        for i in range (q,n):
            if (i==q):
                L[i][q]=1
            else:
                sum = 0
                for k in range(q):
                    sum = sum + L[i][k]*U[k][q]
                    L[i][q] = (A[i][q] - sum)/U[q][q]
    return L, U   

L, U = decompos(A)
print("Matrix L: "+show(L))
print("Matrix L: "+show(U))