def square_matrix_simple(matrix=[]):
    if matrix:
        return [[x**2 for x in row] for row in matrix]
    return None
