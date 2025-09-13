
def fizzbuzz():
    """
    Print numbers from 1 to 100 respecting FizzBuzz rules
    """
    result = []
    # PS: Of course we could do a one liner but this is more readable imo
    for i in range(1, 101):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def fizzbuzz_bonus(input):
    """
    Print numbers from 1 to 100 with custom input.
    Example: {'3': 'Fizz', '5': 'Buzz', '3/5': 'FizzBuzz'} should return the same as fizzbuzz()
    """
    # First we convert keys to list of divisors
    processed_input = []
    for key, word in input.items():
        divisors = [int(k) for k in key.replace("&", "/").split("/")]
        processed_input.append((divisors, word))

    # Then we do a desceding sort for input by number of divisors to ensure combined rules (i.e 3/5 ) are checked first
    processed_input.sort(key=lambda x: -len(x[0]))

    result = []
    for i in range(1, 101):
        output = ""
        for divisors, word in processed_input:
            if all(i % d == 0 for d in divisors):
                output = word
                break
        result.append(output if output else str(i))
    return result

if __name__ == "__main__":
    print("----- Standard FizzBuzz -----\n")
    print(fizzbuzz())

    print("\n----- Bonus FizzBuzz -----\n")
    print(fizzbuzz_bonus({"3": "Fizz", "5": "Buzz", "3&5": "FizzBuzz"}))