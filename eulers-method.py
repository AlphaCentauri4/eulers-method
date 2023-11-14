import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
from scipy.signal import argrelextrema

def eulers_method(equation, initial_cond, xmax, n):
    x0, y0 = (initial_cond)

    equation = equation.replace("x", "x[k-1]").replace("y", "y[k-1]")

    step_h = (xmax-x0)/(n-1)
    x = np.linspace(x0, xmax, n)
    y = np.zeros([n])
    y[0] = y0
    for k in range(1, n):
        y[k] = eval(f"y[k-1] + step_h*({equation})")

    return x, y

def rmse(true, pred):
    return mean_squared_error(true, pred, squared=False)

def nrmse(true, pred):
    return mean_squared_error(true, pred, squared=False)/float(true.mean())

class EvaluationTable:
    def __init__(self, metrics, index_col="model"):
        self.metric_names = metrics.keys()
        self.metric_funcs = metrics.values()
        self.table = pd.DataFrame(columns=self.metric_names)

    def addEvaluation(self, name, true, pred):
        metric_results = []
        for metric in self.metric_funcs:
            metric_results.append(metric(true, pred))
        self.table.loc[name] = metric_results

    def loadTable(self):
        return self.table

# Example
x, y = eulers_method(equation="0.1*(np.sqrt(y)) + 0.4*(np.power(x, 2))",
                     initial_cond=(2, 4),
                     xmax=2.5,
                     n=101
                     )

plt.plot(x, y, label="Predicted")
plt.xlabel("x-value")
plt.ylabel("y-value")
plt.title("Approximate Solution with Euler's Method")
plt.savefig("figures/example-n101.png")
plt.close()

metrics = {"rmse": rmse,
           "nrmse": nrmse,
           "r_squared": r2_score}

euler_evals = EvaluationTable(metrics)

# Task 2
for n in range(101, 502, 100):
    x, y = eulers_method(equation="np.divide(x**2*np.sin(x)+y, x)",
                        initial_cond=(-np.pi/2, 0),
                        xmax=10,
                        n=n
                        )
    plt.plot(x, y, label="Predicted")
    plt.xlabel("x-value")
    plt.ylabel("y-value")
    plt.title("Approximate Solution with Euler's Method")

    t = np.linspace(-np.divide(np.pi, 2), 10., n)
    a = -t*(np.cos(t))

    plt.plot(t, a, label="Observed")

    euler_evals.addEvaluation(f"n={n}", a, y)

    plt.savefig(f"figures/task1-2-n{n}.png")
    plt.close()

results = euler_evals.loadTable()
results.to_csv("results/evaluation_results.csv")
results.plot()

plt.plot()
plt.savefig("figures/performance_by_n.png")
plt.close()