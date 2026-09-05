def markRow(matrix, row):
    cols = len(matrix[0])

    for j in range(cols):
        if matrix[row][j] != 0:
            matrix[row][j] = float("inf")


def markCol(matrix, col):
    rows = len(matrix)

    for i in range(rows):
        if matrix[i][col] != 0:
            matrix[i][col] = float("inf")


rows, cols = map(int, input().split())

matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)


# Find the original zeroes
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            markRow(matrix, i)
            markCol(matrix, j)


# Convert infinity to zero
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == float("inf"):
            matrix[i][j] = 0


# Print matrix
for row in matrix:
    print(row)