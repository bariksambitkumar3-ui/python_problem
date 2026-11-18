from scipy.optimize import minimize
def objective(x):
    return (x[0]-50)**2
result=minimize(
    objective,
    x0=[10],
    bounds=[(0,100)]
)
print(result.x)