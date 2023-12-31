#prime an even numbers
def is_prime(number):
    if number < 2:
        return False

    # Check for factors from 2 to the square root of the given number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
