def sum_of_matrix(matrix1,matrix2):
	result=[]
	for i in range(len(matrix1)):
		row=[]
		for j in range(len(matrix1[i])):
			row.append(matrix1[i][j]+matrix2[i][j])
		result.append(row)

	return result

def create_matrix(m,n):
	matrix=[]
	for i in range(m):
		temp=0
		row=[]
		while(temp!=n):
			print("Row ",i+1,":",end="")
			row = list(map(int,input().split()))
			temp=len(row)
		matrix.append(row)
	return matrix


def display(matrix):
	for i in matrix:
		for j in i:
			print(j,end=" ")
		print()
	print()
print("NOTE:Enter Dimensions with sapce in between\nEg: 5 x 4 as 5 4\n")

m1=m2=n1=n2=0

print("Matrix 1:")
m1,n1 = map(int,(input("Dimensions(MxN):").split()))

matrix1= create_matrix(m1,n1)
print("matrix 1:")
display(matrix1)

while(m1!=m2 or n1!=n2):
	print("Matrix 2:")
	m2,n2 = map(int,(input("Dimensions(MxN):").split()))

matrix2 = create_matrix(m2,n2)
print("matrix 2:")
display(matrix2)

result=sum_of_matrix(matrix1,matrix2)
print("Result:")
display(result)