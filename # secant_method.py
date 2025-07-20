# secant_method.py

"""
Secant Method to Find the Root of the Equation f(x) = x^3 - 5x + 1
"""

def f(x):
    """Define the function whose root is to be found."""
    return x**3 - 5*x + 1

def secant(x0, x1, n):
    """Perform the Secant Method for n iterations using initial guesses x0 and x1."""
    i = 1

    while i <= n:
        f0 = f(x0)
        f1 = f(x1)

        if f1 - f0 == 0:
            print(f"Zero division error at iteration {i}. Secant method fails.")
            return

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        fx2 = f(x2)

        # Display iteration details
        print(f"Iteration {i}: x = {x2:.6f}, f(x) = {fx2:.6f}")

        # Update the values for next iteration
        x0, x1 = x1, x2
        i += 1

    print(f"\nRequired root after {n} iterations is approximately: {x2:.6f}")

def main():
    """Main function to take user input and call the Secant method."""
    print("Secant Method to find the root of f(x) = x^3 - 5x + 1")

    try:
        x0 = float(input("Enter first initial guess (x0): "))
        x1 = float(input("Enter second initial guess (x1): "))
        n = int(input("Enter number of iterations: "))

        secant(x0, x1, n)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the program
if __name__ == "__main__":
    main()
