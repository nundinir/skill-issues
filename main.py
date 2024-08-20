import random


def generate_random_number(max_number=10):
    """
    Generate a random number between 1 and max_number.

    Args:
        max_number (int, optional): The maximum number that can be generated. Defaults to 10.
    """
    return random.randint(1, max_number)


def check_even_odd(number):
    if number % 2 == 0:
        print("The number is odd.")
    else:
        print("The number is even.")


def main():
    number = generate_random_number(10)
    print("Generated number:", number)
    check_even_odd(number)


if __name__ == "__main__":
    main()
