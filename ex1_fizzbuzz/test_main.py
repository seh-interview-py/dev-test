import main

def test_fizzbuzz():
    fizzbuzz = main.fizzbuzz()
    assert fizzbuzz[0] == "1"
    assert fizzbuzz[2] == "Fizz"
    assert fizzbuzz[4] == "Buzz"
    assert fizzbuzz[29] == "FizzBuzz"
    assert fizzbuzz[99] == "Buzz"
    print("Successfully passed tests for test_fizzbuzz")

def test_fizzbuzz_bonus():
    input_data = {'4': 'Toto', '7': 'Yoyo', '3/5': 'FizzBuzz'}
    fizzbuzz_bonus = main.fizzbuzz_bonus(input_data)
    assert fizzbuzz_bonus[0] == "1"
    assert fizzbuzz_bonus[3] == "Toto"
    assert fizzbuzz_bonus[6] == "Yoyo"
    assert fizzbuzz_bonus[14] == "FizzBuzz"
    print("Successfully passed tests for test_fizzbuzz_bonus")

if __name__ == "__main__":
    test_fizzbuzz()
    test_fizzbuzz_bonus()