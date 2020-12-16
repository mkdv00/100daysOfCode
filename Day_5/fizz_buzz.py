def main():
    for kid_number in range(1, 101):
        if kid_number % 3 == 0 and kid_number % 5 == 0:
            print("FizzBuzz")
        elif kid_number % 3 == 0:
            print("Fizz")
        elif kid_number % 5 == 0:
            print("Buzz")
        else:
            print(kid_number)


if __name__ == "__main__":
    main()
