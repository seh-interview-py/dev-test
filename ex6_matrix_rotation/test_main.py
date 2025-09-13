import main

def test_rotate_matrix():
    matrix = [
        [1, 2, 3],
        [1, 3, 5],
        [1, 4, 7]
    ]

    # Right rotation 4 times should return original
    result_r4 = main.rotate_matrix(matrix, 4, 'R')
    assert result_r4 == matrix, f"Right rotation 4 failed: got {result_r4} instead of {matrix}"

    # Left rotation 4 times should return original
    result_r5 = main.rotate_matrix(matrix, 4, 'L')
    assert result_r5 == matrix, f"Left rotation 4 failed: got {result_r5} instead of {matrix}"

    # Left rotation 1 time
    result_l = main.rotate_matrix(matrix, 1, 'L')
    expected_l = [
        [3, 5, 7],
        [2, 3, 4],
        [1, 1, 1]
    ]
    assert result_l == expected_l, f"Left rotation 1 failed: got {result_l} instead of {expected_l}"

    # Right rotation 1 time
    result_r = main.rotate_matrix(matrix, 1, 'R')
    expected_r = [
        [1, 1, 1],
        [4, 3, 2],
        [7, 5, 3]
    ]
    assert result_r == expected_r, f"Right rotation 1 failed: got {result_r} instead of {expected_r}"

    # Left rotation 2 times
    result_l2 = main.rotate_matrix(matrix, 2, 'L')
    expected_l2 = [
        [7, 4, 1],
        [5, 3, 1],
        [3, 2, 1]
    ]
    assert result_l2 == expected_l2, f"Left rotation 2 failed: got {result_l2} instead of {expected_l2}"

    # Right rotation 3 times
    result_r3 = main.rotate_matrix(matrix, 3, 'R')
    expected_r3 = [
        [3, 5, 7],
        [2, 3, 4],
        [1, 1, 1]
    ]
    assert result_r3 == expected_r3, f"Right rotation 3 failed: got {result_r3} instead of {expected_r3}"


if __name__ == "__main__":
    test_rotate_matrix()
    print("Successfully passed tests for test_rotate_matrix")
