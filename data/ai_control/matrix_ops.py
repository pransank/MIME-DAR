"""
Basic matrix operations implemented without external libraries.
"""

from typing import List

Matrix = List[List[float]]


def matrix_add(a: Matrix, b: Matrix) -> Matrix:
    """Add two matrices of the same dimensions."""
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matrix_multiply(a: Matrix, b: Matrix) -> Matrix:
    """Multiply two matrices."""
    rows_a, cols_a = len(a), len(a[0])
    cols_b = len(b[0])

    result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result


def transpose(matrix: Matrix) -> Matrix:
    """Transpose a matrix."""
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print(matrix_add(m1, m2))
    print(matrix_multiply(m1, m2))
