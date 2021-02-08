"""
This program is so that I don't have to manually do
a floyd warshal demonstration on every bloody step
of the matrix.
"""

def printmat(mat: list):
    for sublist in mat:
        print(sublist)
    print("\n\n")

def floyd_warsh(matrix: list, n: int):

    for a in range(n):
        for b in range(n):
            for c in range(n):
                if (matrix[b][a] is None) or (matrix[a][c] is None):
                    pass
                elif matrix[b][c] is None:
                    matrix[b][c] = matrix[b][a] + matrix[a][c]
                    pass
                elif matrix[b][c] > matrix[b][a] + matrix[a][c]:
                    matrix[b][c] = matrix[b][a] + matrix[a][c]
        printmat(matrix)
