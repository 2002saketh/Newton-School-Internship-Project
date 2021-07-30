# A simple Python program to
# find sum of diagonals
MAX = 100

def printDiagonalSums(mat, n):

	principal = 0
	secondary = 0;
	for i in range(0, n):
		for j in range(0, n):

			# Condition for principal diagonal
			if (i == j):
				principal += mat[i][j]

			# Condition for secondary diagonal
			if ((i + j) == (n - 1)):
				secondary += mat[i][j]
		
	print("Principal Diagonal:", principal)
	print("Secondary Diagonal:", secondary)

# Driver code
row=int(input("Enter number of rows you want: "))
col=int(input("Enter number of columns you want: "))
mat=[]
for m in range(row):
  a=[]
  for n in range(col):
     a.append(0)
  mat.append(a)

for i in range(len(mat)):
  for j in range(len(mat[0])):
    mat[i][j]=int(input("Input element: "))
print("Your Matrix is :",mat)
printDiagonalSums(mat, row)
