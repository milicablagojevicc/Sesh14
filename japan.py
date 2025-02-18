def cook():
    print("we are making sushi")


def is_prime(number):
    """
    Checks if a number is prime.
    :param number: The number to test.
    :return: True if prime, False if not.
    """
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False  # not a prime number
    return True

if __name__ == "__main__":
    print("testing my function")
    assert is_prime(5) is True, "Error in function, 5 is prime"
    assert is_prime(6) is False, "Error in function, 6 is not prime"
    assert is_prime(7) is True, "Error in function, 7 is prime"
    print(is_prime(5))
    print(is_prime(7))
    print(is_prime(9))