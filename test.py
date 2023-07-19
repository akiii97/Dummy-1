def addition():
    print("Enter numbers for addition")

    while True:
        try:
            num1 = float(input('Enter First Number: '))
            num2 = float(input('Enter Second Number: '))
            result = num1 + num2
            print("The answer to the added value is", result)
            break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            print("merging")


addition()


def subtraction():
    print("Enter numbers for Division")

    while True:
        try:
            num1 = float(input('Enter First Number: '))
            num2 = float(input('Enter Second Number: '))
            result = num1 - num2
            print("The answer to the subtracted value is", result)
            break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")


subtraction()


def division():
    print("Enter numbers for Division")

    while True:
        try:
            num1 = float(input('Enter First Number: '))
            num2 = float(input('Enter Second Number: '))
            result = num1 / num2
            print("The answer to the divided value is", result)
            break  # Exit the loop if division is successful
        except ValueError:
            print("Invalid input! Please enter valid numbers.")


division()


def multiplication():
    print("Enter numbers for Multiplication")

    while True:
        try:
            num1 = float(input('Enter First Number: '))
            num2 = float(input('Enter Second Number: '))
            result = num1 * num2
            print("The answer to the multiplied value is", result)
            break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")


multiplication()

print("All done")
