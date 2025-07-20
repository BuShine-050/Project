# false_position_method.py

"""
False Position Method (Regula Falsi) to Find the Root of the Equation f(x) = x^3 - 5x + 1
"""

def f(x):
    """Define the function whose root is to be found."""
    return x**3 - 5*x + 1

def false_position(a, b, n):
    """Perform the False Position Method for n iterations between interval [a, b]."""
    i = 1
    x = a  # Initialize x

    while i <= n:
        fa = f(a)
        fb = f(b)

        # Compute the false position
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)

        # Display iteration details
        print(f"Iteration {i}: x = {x:.6f}, f(x) = {fx:.6f}")

        # Update the interval based on sign of f(x)
        if fa * fx < 0:
            b = x
        else:
            a = x

        i += 1

    print(f"\nRequired root after {n} iterations is approximately: {x:.6f}")

def main():
    """Main function to take user input and call the false position method."""
    print("False Position Method to find the root of f(x) = x^3 - 5x + 1")

    try:
        a = float(input("Enter first approximation (a): "))
        b = float(input("Enter second approximation (b): "))
        n = int(input("Enter number of iterations: "))

        if f(a) * f(b) > 0:
            print("Given values do not bracket a root.")
            print("Try again with values where f(a) and f(b) have opposite signs.")
        else:
            false_position(a, b, n)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the program
if __name__ == "__main__":
    main()
