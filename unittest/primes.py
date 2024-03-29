def is_prime(number):
    if number <= 1:
        return False


    if number in (0, 1):
        return False

    """Return True if *number* is prime."""
    for element in range(2,number):
        if number % element == 0:
            return False

    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
