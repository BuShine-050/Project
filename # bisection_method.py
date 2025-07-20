# bisection_method.py

"""
Bisection Method to Find the Root of the Equation f(x) = x^3 - 5x + 1

"""

def f(x):
    """Define the function whose root is to be found."""
    return x**3 - 5*x + 1

def bisection(a, b, n):
    """Perform the Bisection Method for n iterations between interval [a, b]."""
    i = 1
    while i <= n:
        x = (a + b) / 2
        fx = f(x)

        # Update interval
        if fx < 0:
            a = x
        else:
            b = x

        # Display iteration details
        print(f"Iteration {i}: x = {x:.6f}, f(x) = {fx:.6f}")

        i += 1

    print(f"\nRequired root after {n} iterations is approximately: {x:.6f}")

def main():
    """Main function to take user input and call the bisection method."""
    print("Bisection Method to find the root of f(x) = x^3 - 5x + 1")

    try:
        a = float(input("Enter first approximation (a): "))
        b = float(input("Enter second approximation (b): "))
        n = int(input("Enter number of iterations: "))

        if f(a) * f(b) > 0:
            print("Given values do not bracket a root.")
            print("Try again with values where f(a) and f(b) have opposite signs.")
        else:
            bisection(a, b, n)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the program
if __name__ == "__main__":
    main()
