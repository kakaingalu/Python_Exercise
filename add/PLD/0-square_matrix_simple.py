#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Function that prints square of matrix"""
    New_list = []
    for row in matrix:
        row_matrix = []
        for element in row:
            row_matrix.append(element**2)
        New_list.append(row_matrix)
    return New_list
