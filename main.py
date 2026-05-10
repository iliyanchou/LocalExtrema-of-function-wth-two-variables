import sympy as smp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



x, y = smp.symbols('x y')

f = x**2 + y**2 # funkciq

firstOrderDiff = [
    smp.diff(f, x),
    smp.diff(f, y)
]

critPoint = smp.solve(firstOrderDiff, (x, y), dict=True)

HusMat = smp.hessian(f, (x, y))

if isinstance(critPoint, list):
    indeciesOfCritPoints = []
    indeciesOfSedPoints = []
    for i in range(len(critPoint)):
        d = float(HusMat.subs(critPoint[i]).det().evalf())
        if d > 0:
            indeciesOfCritPoints.append(i)
        elif d < 0:
            indeciesOfSedPoints.append(i)
            
    if len(indeciesOfCritPoints) > 0:
        print("The points:", end=" ")
        for i in range(len(indeciesOfCritPoints)):
            print(str(critPoint[indeciesOfCritPoints[i]]), end=" ")
        print("\n are stationary.")
        print("The function: " + str(f) + " , reaches as it follows:", end=" ")
        for i in range(len(indeciesOfCritPoints)):
            checkf = float(HusMat[0, 0].subs(critPoint[indeciesOfCritPoints[i]]).evalf())
            if checkf > 0:
                print("local min which is: " + str(f.subs(critPoint[indeciesOfCritPoints[i]]).evalf()), end=" ")
            elif checkf < 0:
                print("local max which is: " + str(f.subs(critPoint[indeciesOfCritPoints[i]]).evalf()), end=" ")
        print("\n")
        
    if len(indeciesOfSedPoints) > 0:
        print("The points:", end=" ")
        for i in range(len(indeciesOfSedPoints)):
            print(str(critPoint[indeciesOfSedPoints[i]]), end=" ")
        print("\n are saddle points and the function " + str(f) + " does not reach local extrema there.")

else:
    d = float(HusMat.subs(critPoint).det().evalf())
    if d > 0:
        print("The point: " + str(critPoint) + " is stationary.")
        checkf = float(HusMat[0, 0].subs(critPoint).evalf())
        if checkf > 0:
            print("The function: " + str(f) + " ,reaches local minimum there which is: " + str(f.subs(critPoint).evalf()))
        elif checkf < 0:
            print("The function: " + str(f) + " ,reaches local max there which is: " + str(f.subs(critPoint).evalf()))
    elif d < 0:
        print("The point: " + str(critPoint) + " is saddle point and the function " + str(f) + " does not reach local extrema there.")



f_num = smp.lambdify((x, y), f, "numpy")

x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f_num(X, Y)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

ax.set_title(f"Графика на {f}")
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

fig.colorbar(surface, shrink=0.5, aspect=5)

plt.show()