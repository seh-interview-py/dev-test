def my_sum(numbers):
    """
    Recursively sum a list of given numbers
    :param numbers: list of numbers
    :return: sum of the numbers
    """
    if not numbers:
        return 0
    return numbers[0] + my_sum(numbers[1:])  # sum first element and the rest of the elements

if __name__ == "__main__":
    my_numbers = [1, 2, 3, 4, 5]
    print("Sum of", my_numbers, "is:", my_sum(my_numbers))

