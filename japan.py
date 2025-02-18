def cook():
    print("I am making sushi")

def is_prime(number):
        """
        Checks if a number is prime
        :param number: the no to test
        :return: true if prime, false if not
        """
        for i in range(2, number//2+1):
            if number % i == 0:
                return False #not prime
        return True

if __name__ == "__main__":
    print("testing function:")
    assert is_prime(5)is True, "Error in function, 5 is prime"
    assert is_prime(6) is False, "Error in function, 6 is NOT prime"
    assert is_prime(7) is True, "Error in function, 7 is prime"