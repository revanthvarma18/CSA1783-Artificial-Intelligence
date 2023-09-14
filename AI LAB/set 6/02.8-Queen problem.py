print ("enter the number")
N = int(input())
list= [[0]*N for _ in range(N)]
def attack(i, j):
    for k in range(0,N):
        if list[i][k]==1 or list[k][j]==1:
            return True
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if list[k][l]==1:
                    return True
    return False
def N_queens(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(attack(i,j))) and (list[i][j]!=1):
                list[i][j] = 1
                if N_queens(n-1)==True:
                    return True
                list[i][j] = 0
    return False
N_queens(N)
for i in list:
    print (i)