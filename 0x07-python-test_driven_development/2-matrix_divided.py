#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same sizeEach row of the matrix must have the same size")
    if not isinstance (div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zerodivision by zero")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                new_max_divided.pyZZtrix = matrix[i][j] / div
                rounded = round (new_marix, 2)
                return rounded
