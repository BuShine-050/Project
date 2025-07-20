# newton_raphson_method.py

"""
Newton-Raphson Method to Find the Root of the Equation f(x) = x^3 - 5x + 1
"""

def f(x):
    """Define the function whose root is to be found."""
    return x**3 - 5*x + 1

def df(x):
    """Define the derivative of the function f(x)."""
    return 3*x**2 - 5

def newton_raphson(x0, n):
    """Perform the Newton-Raphson Method for n iterations starting from initial guess x0."""
    i = 1
    x = x0

    while i <= n:
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            print(f"Derivative zero at iteration {i}, method fails.")
            return

        x_new = x - fx / dfx

        # Display iteration details
        print(f"Iteration {i}: x = {x_new:.6f}, f(x) = {f(x_new):.6f}")

        x = x_new
        i += 1

    print(f"\nRequired root after {n} iterations is approximately: {x:.6f}")

def main():
    """Main function to take user input and call the Newton-Raphson method."""
    print("Newton-Raphson Method to find the root of f(x) = x^3 - 5x + 1")

    try:
        x0 = float(input("Enter initial guess (x0): "))
        n = int(input("Enter number of iterations: "))
        newton_raphson(x0, n)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the program
if __name__ == "__main__":
    main()
