from pandas import Series
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_linear_regression(data1: Series, data2: Series):
    model = LinearRegression()

    x = pd.DataFrame(data1)
    y = pd.DataFrame(data2)

    model.fit(x, y)

    model.coef_
    model.intercept_

    plt.figure(figsize=(10, 6))
    plt.title("Линейная регрессия", fontsize=16, fontweight="bold", color="black")
    plt.scatter(data1, data2, alpha=0.4)

    plt.plot(x, model.predict(x), color = 'r', linewidth = 2)

    plt.xlabel(data1.name)
    plt.ylabel(data2.name)
    plt.ylim(data2.min(), data2.max())
    plt.xlim(data1.min(), data1.max())

    plt.show()

