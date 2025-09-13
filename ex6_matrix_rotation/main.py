def rotate_matrix(matrix, rotations, direction):
    """
    Rotate a matrix 90 degrees left or right 'rotations' times
    :param matrix: list of lists representing the matrix
    :param rotations: number of 90 degree rotations
    :param direction: L or R for left or right
    """
    if not matrix or not matrix[0]:
        return matrix

    # if number of rotations is multiple of 4, return original matrix
    rotations = rotations % 4
    if rotations == 0:
        return matrix

    rotated = matrix
    for _ in range(rotations):
        # n will represent number of rows and m number of columns in the original matrix
        n = len(rotated)
        m = len(rotated[0])
        # Here we swap rows and columns
        new_matrix = [[0] * n for _ in range(m)]
        # We might optimize this part by avoiding nested loops using "zip" as far as i saw online
        for i in range(n):
            for j in range(m):
                if direction.upper() == 'R':
                    new_matrix[j][n - 1 - i] = rotated[i][j]
                elif direction.upper() == 'L':
                    new_matrix[m - 1 - j][i] = rotated[i][j]
                else:
                    raise ValueError("Direction must be either 'L' or 'R'")
        rotated = new_matrix

    return rotated


if __name__ == "__main__":
    sample_matrix = [
        [1,2,3],
        [1,3,5],
        [1,4,7]
    ]
    print("Original Matrix:")
    for row in sample_matrix:
        print(row)

    print("\nMatrix rotated 90 degrees to the left:")
    rotated_left = rotate_matrix(sample_matrix, 1, 'L')
    for row in rotated_left:
        print(row)


