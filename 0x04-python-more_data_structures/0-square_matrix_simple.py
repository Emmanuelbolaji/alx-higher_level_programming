#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    squared_matrix = (squares ** 2 for squares in new_matrix)
    print(squared_matrix)
