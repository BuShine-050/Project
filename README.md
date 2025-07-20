# 🔍 Root Finding Methods in Python

This project demonstrates how to find approximate roots of nonlinear equations using classical **numerical methods** in Python. All four methods are implemented as standalone programs for the function:

Each program allows user input and prints step-by-step iterations to show how the root converges.

---

## 📂 Folder Structure
root-finding-methods/
├── bisection_method.py
├── false_position_method.py
├── newton_raphson_method.py
├── secant_method.py
└── README.md


---

## 1️⃣ Bisection Method

### 📌 Description
- A **bracketing method** that repeatedly halves the interval `[a, b]` until the root is located with desired accuracy.
- Guarantees convergence if `f(a)` and `f(b)` have opposite signs.

### 📐 Formula
x = {a + b}/{2}

### 📥 Input Required
- `a`, `b` (such that `f(a) * f(b) < 0`)
- Number of iterations `n`

### ▶️ Run
```bash
python bisection_method.py
```

## 2️⃣ False Position Method (Regula Falsi)

### 📌 Description
-Another bracketing method, but instead of using the midpoint, it draws a secant line between (a, f(a)) and (b, f(b)) and computes where it crosses the x-axis.
-Often converges faster than bisection.

### 📐 Formula
x = (a * f(b) - b * f(a)) / (f(b) - f(a))

### 📥 Input Required
- `a`, `b` (such that `f(a) * f(b) < 0`)
- Number of iterations `n`

### ▶️ Run
```bash
python false_position_method.py
```
## 3️⃣ Newton-Raphson Method

### 📌 Description
-An open method that uses the first derivative of the function. Starting from an initial guess x0, it iteratively applies the formula to approach the root.
-Generally converges faster (quadratically) if the initial guess is close, but requires the function’s derivative and a good starting point.

### 📐 Formula
The Newton-Raphson iteration is
x_{n+1} = x_n - f(x_n) / f'(x_n)

f'(x) is the derivative of the function f(x).
For the function:
f(x) = x^3 - 5x + 1

the derivative is:
f'(x) = 3x^2 - 5

### 📥 Input Required
-Initial guess `x0`.
-Number of iterations `n`.

###  ▶️ Run
```bash
python newton_raphson_method.py
```
## 4️⃣ Secant Method

### 📌 Description
An open method similar to the false position method but without bracketing. It uses two initial guesses and does not require the derivative of the function.
Often converges faster than simple bracketing methods and does not need computation of 𝑓′.

### 📐 Formula
Starting with initial guesses 𝑥0 and x1,each new approximation is given by
x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))

### 📥 Input Required
Two initial guesses `x0` and `x1`.
Number of iterations `n`.

###  ▶️ Run
```bash
python secant_method.py
```

 
