# Multi-Variable Calculus Solver & Visualizer 🧮📊

A Python-based tool for automated analysis and 3D visualization of functions with two variables ($x$ and $y$). Powered by **SymPy**, this script finds critical points, computes the Hessian matrix, classifies local extrema, and generates interactive plots.

## 🚀 Features

* **Symbolic Differentiation:** Automatically generates first and second-order partial derivatives using SymPy's `hessian` and `diff` engines.
* **Critical Point Discovery:** Solves systems of equations to find all stationary points.
* **Hessian Analysis:** Uses the second derivative test (Sylvester's criterion) to classify:
    * **Local Minima**
    * **Local Maxima**
    * **Saddle Points**
* **3D Visualization:** Generates interactive surface plots using **Matplotlib** and **NumPy** to visually confirm mathematical findings.
* **Numerical Precision:** Supports complex trigonometric and exponential functions using `.evalf()` and `lambdify`.

## 📦 Requirements

* **Python 3.10+** (Optimized for Python 3.14 on macOS)
* **SymPy** (Symbolic math)
* **NumPy** (Numerical arrays)
* **Matplotlib** (3D Plotting)

## 🛠️ Installation & Setup

1. **Clone the repository and navigate to the project folder:**
   ```bash
   git clone https://github.com/iliyanchou/LocalExtrema-of-function-wth-two-variables.git
   cd LocalExtrema-of-function-wth-two-variables

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .\.venv\Scripts\activate  # Windows


3. Install dependencies:
   ```bash
   pip install sympy numpy matplotlib
4. Run the script:
   ```bash
   python3 main.py
## 📖 Usage
Open `main.py` and modify the function `f`.

**Example:**
```python
f = smp.sin(x) * smp.sin(y)
```
The script will:
* **Print** the classification of every critical point in the terminal.
* **Open** an interactive 3D window showing the function's surface.

## 📝 Sample Output
```text
The points: {x: 0, y: 0} 
are stationary.
The function: x**2 + y**2 , reaches as it follows: local min which is: 0
```
## 🛠️ Roadmap
- [x] Add Matplotlib integration for 3D surface plotting.
- [ ] Extend support for functions with $n$ variables.
- [ ] Implement automatic marking of critical points on the 3D plot.
- [ ] Export results to LaTeX or PDF reports.


Developed by: Iliya Granchulov 🚗💨
