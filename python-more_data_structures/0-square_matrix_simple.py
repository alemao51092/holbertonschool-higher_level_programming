#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for row in matrix:
        squarerow = [num ** 2 for num in row]
        newmatrix.append(squarerow)
    return newmatrix
