#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_mat = [[(e * e) for e in row] for row in matrix]
    return new_mat
