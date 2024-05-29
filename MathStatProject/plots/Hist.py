import matplotlib.pyplot as plt
from pandas import Series
import seaborn as sns

def plot_hist(data: Series, bins):
    plt.figure(figsize=(10, 6))
    sns.histplot(data, kde=True, stat="density", bins=bins)

    plt.title('Гистограмма с графиком функции распределения')
    plt.xlabel(data.name)
    plt.ylabel('Частота')

    plt.show()