import random


def generate_random_number(max_number=2000):
    """
    Generate a random number between 1 and max_number.

    Args:
        max_number (int, optional): The maximum number that can be generated. Defaults to 10.
    """
    
    return random.randint(1, max_number)


def check_even_odd(number):
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


def main():
    max_num = int(input("Input the maximum number to generate: "))
    
    number = generate_random_number(max_num)
    print("Generated number:", number)
    check_even_odd(number)


if __name__ == "__main__":
    main()
