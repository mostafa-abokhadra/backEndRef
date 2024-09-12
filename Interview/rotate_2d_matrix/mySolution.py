#!/usr/bin/python3
""" rotating a matrix 90-Degree
"""


def rotate_2d_matrix(matrix):
    """rotate the matrix function

    Args:
        matrix: 2d array
    """

    i = 0
    column_idx = 0
    new_arr = []
    rotated_matrix = []
    while(i < len(matrix)):
        new_arr.append(matrix[i][column_idx])
        if i == len(matrix) - 1:
            new_arr.reverse()
            rotated_matrix.append(list(new_arr))
            new_arr.clear()
            column_idx += 1
            if column_idx == len(matrix):
                break
            i = 0
            continue
        i += 1

    for i in range(len(rotated_matrix)):
        for j in range(len(rotated_matrix)):
            matrix[i][j] = rotated_matrix[i][j]
