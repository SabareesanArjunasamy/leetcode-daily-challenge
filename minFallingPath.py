'''Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

'''


def minFallingPathSum(matrix):
    length = len(matrix)
    for row in range(1, length):
        preRow = matrix[row - 1]
        for column in range(0, length):
            matrix[row][column] += min(
                preRow[max(0, column - 1)],
                preRow[column],
                preRow[min(column + 1, length - 1)]
            )
    return min(matrix[length - 1])


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(minFallingPathSum(matrix))

matrix2 = [[-19, 57], [-40, -5]]
print(minFallingPathSum(matrix2))
