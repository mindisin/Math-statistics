import matplotlib.pyplot as plt
import numpy as np

def scatter_plot(data1, data2):
    # Создание диаграммы рассеивания
    plt.scatter(data1, data2, alpha = 0.4)

    # Настройка меток и заголовка
    plt.xlabel(data1.name)
    plt.ylabel(data2.name)
    plt.title('Диаграмма рассеивания')

    # Отображение графика
    plt.show()