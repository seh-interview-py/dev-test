def game_of_life(matrix, iterations=5):
    """
    Counts neighbors and only sets cell to alive if it has exactly 3 neighbors
    """
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0

    for _ in range(iterations):
        # Create a new matrix to store results
        new_matrix = [[0] * columns for _ in range(rows)]

        for r in range(rows):
            for c in range(columns):
                # Count alive neighbors
                neighbors = 0
                for i in range(max(0, r-1), min(rows, r+2)):
                    for j in range(max(0, c-1), min(columns, c+2)):
                        if i == r and j == c:
                            continue
                        if matrix[i][j] == 1:
                            neighbors += 1

                # only bring dead cells to life if exactly 3 neighbors
                if neighbors == 3:
                    new_matrix[r][c] = 1
                else:
                    new_matrix[r][c] = matrix[r][c]  # otherwise we keep current state

        matrix = new_matrix

        # Welp, i gave up here -__-"

    html = "<table border='1'>\n"
    for row in matrix:
        html += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>\n"
    html += "</table>"
    print(html)

    return matrix


if __name__ == "__main__":
    initial_matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1]
    ]
    print("Initial Matrix:")
    for row in initial_matrix:
        print(row)

    print("\nMatrix after applying Game of Life:")
    result_matrix = game_of_life(initial_matrix, iterations=5)
    for row in result_matrix:
        print(row)

