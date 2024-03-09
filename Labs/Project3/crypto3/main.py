import math

# Function to calculate the greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def pollards_rho(n, f):
    x, y, d = 2, 2, 1
    j = 1

    # Loop until a non-trivial divisor is found
    while d == 1:
        # Generate sequence values using the provided function
        x = f(x) % n
        y = f(f(y)) % n

        # Update d using the GCD of the absolute difference between x and y and n
        d = gcd(abs(x - y), n)

        # If a non-trivial divisor is found, return it
        if 1 < d < n:
            return d

        # Increment the iteration counter
        j += 1

    return None


def get_user_defined_function(n):
    user_input = input("Enter the user-defined function f(x) (e.g., x**2 + x + 1): ")
    user_defined_function = lambda x: eval(user_input) % n
    return user_defined_function


def main():
    n = int(input("Enter the number to factorize: "))

    print("Choose an option:")
    print("1. Use implicit function f(x) = x^2 + 1")
    print("2. Enter a custom user-defined function")

    option = input("Enter option (1 or 2): ")

    if option == '1':
        user_defined_function = lambda x: (x ** 2 + 1) % n
    elif option == '2':
        user_defined_function = get_user_defined_function(n)
    else:
        print("Invalid option. Please enter 1 or 2.")
        return

    result = pollards_rho(n, user_defined_function)
    if result:
        print(f"Nontrivial factor found: {result}")
    else:
        print("No nontrivial factor found.")


if __name__ == "__main__":
    main()
