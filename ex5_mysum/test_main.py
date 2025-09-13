import main

def test_my_sum():
    test_list = [1, 2, 3, 4, 5]
    test_list_with_negative_values = [10.5, 2.5, -3, 7]
    test_empty_list = []
    test_list_one_value = [6]

    assert main.sum_recursive_optimized(test_list) == 15
    assert main.sum_recursive_optimized(test_list_with_negative_values) == 17.0
    assert main.sum_recursive_optimized(test_empty_list) == 0
    assert main.sum_recursive_optimized(test_list_one_value) == 6

if __name__ == "__main__":
    test_my_sum()
    print("Successfully passed tests for test_my_sum")