def mltpl_mtrx(A, B):
    if len(A[0]) != len(B):
        return "Matrices cannot be multiplied"

    result = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example usage:
matrix_A = [[1, 2, 3], [4, 5, 6]]  # 2x3 matrix
matrix_B = [[7, 8], [9, 10], [11, 12]]  # 3x2 matrix

result_matrix = mltpl_mtrx(matrix_A, matrix_B)
print(result_matrix)
