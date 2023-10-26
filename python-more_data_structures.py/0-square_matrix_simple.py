#!/usr/bin/python3
def square_matrix_simple(matrix):
    # Create an empty result matrix of the same size as the input matrix
    result = []

    for row in matrix:
        squared_row = []  # Create a new row for the result matrix
        for value in row:
            squared_row.append(value ** 2)  # Square each value and add to the new row
        result.append(squared_row)  # Add the new row to the result matrix

    return result
