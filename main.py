"""
Group:
NAME: Avishag Tamsut ID: 326275609
NAME: Sahar Emmona ID: 213431133
NAME: Merav Hashta ID: 214718405
"""
def initialize_matrix(n):
    """
    This function reset matrix.
    """
    matrix = [[0 for i in range(n)] for j in range(n)]
    return matrix

def print_matrix(matrix):
    """
    This function print matrix.
    """
    for row in matrix:
     print(row)

def sum_matrices(matrix_a, matrix_b):
  """
  This function return the sum of matrices.
  """
  n = len(matrix_a)
  sum_matrix = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
    for j in range(n):
         sum_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]
  return sum_matrix

def multiply_matrices(matrix_a, matrix_b):
  """
  This function return multiply of matrices.
  """
  n = len(matrix_a)
  multy_matrix = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        multy_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
  return multy_matrix

# receives from user the length of matrix 2x2.
n = int(input("Enter the length of square matrix:"))

# create 2 matrix.
matrix_a = initialize_matrix(n)
matrix_b = initialize_matrix(n)

# receiving values for matrices from the user
for i in range(n):
  for j in range(n):
    matrix_a[i][j] = int(input(f"Fill matrix A [{i}, {j}]: "))
for i in range(n):
  for j in range(n):
    matrix_b[i][j] = int(input(f"Fill matrix B [{i}, {j}]: "))

# print matrix A,B:
print("Matrix A:")
print_matrix(matrix_a)

print("Matrix B:")
print_matrix(matrix_b)

# print sum of matrix A,B:
sum_matrix = sum_matrices(matrix_a, matrix_b)
print("The sum of matrix A,B:")
print_matrix(sum_matrix)

# print multy matrix A,B:
product_matrix = multiply_matrices(matrix_a, matrix_b)
print("The multy matrix A,B:")
print_matrix(product_matrix)