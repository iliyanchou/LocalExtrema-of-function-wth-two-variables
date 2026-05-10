# Multi-Variable Calculus Solver 🧮

A Python-based tool for automated analysis of functions with two variables ($x$ and $y$). Powered by **SymPy**, this script finds critical points, computes the Hessian matrix, and classifies local extrema.

## 🚀 Features

* **Symbolic Differentiation:** Automatically generates first and second-order partial derivatives.
* **Critical Point Discovery:** Solves systems of equations to find all stationary points.
* **Hessian Analysis:** Uses the second derivative test (Sylvester's criterion) to classify:
    * Local Minima
    * Local Maxima
    * Saddle Points
* **Numerical Precision:** Supports trigonometric and exponential functions using `.evalf()` and `float()` conversion for robust logic.

## 📦 Requirements

* **Python 3.10+** (Tested on Python 3.14)
* **SymPy** (for symbolic mathematics)

## 🛠️ Installation & Setup

1.  **Clone the repository and navigate to the project folder:**
    ```bash
    git clone [https://github.com/yourusername/sympMath.git](https://github.com/yourusername/sympMath.git)
    cd sympMath
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # For macOS/Linux
    # .\.venv\Scripts\activate  # For Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install sympy
    ```

4.  **Run the script:**
    ```bash
    python3 funcExtr.py
    ```

## 📖 Usage

Modify the function `f` in `funcExtr.py` to analyze different surfaces.

**Example (Saddle Point):**
```python
f = x**2 - y**2




Example (Trigonometric Surface):

Python
f = smp.sin(x) * smp.sin(y)
The script will iterate through all detected critical points and print the classification results in the terminal.

📝 Sample Output
Plaintext
The points: {x: 0, y: 0} 
are stationary.
The function: sin(x)*sin(y) reaches as it follows: local max which is: 1.00000000000000






🛠️ Roadmap
[ ] Add Matplotlib integration for 3D surface plotting.
[ ] Extend support for functions with $n$ variables.
[ ] Export results to LaTeX or PDF reports.
