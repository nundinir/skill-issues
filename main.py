import random


def generate_random_number():
    return random.randint(1, 10)


def check_even_odd(number):
    if number % 2 == 0:
        print("The number is odd.")
    else:
        print("The number is even.")


def main():
    number = generate_random_number()
    print("Generated number:", number)
    check_even_odd(number)


if __name__ == "__main__":
    main()
