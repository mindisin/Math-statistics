from pandas import Series
from constants import round_digits_count
from handlers.Mean import get_mean
from handlers.NoDisplacedDispersion import get_no_displaced_dispersion
from handlers.SampleSize import get_sample_size
import scipy.stats as stats
from scipy.stats import shapiro
from scipy.stats import skew

def hypothesis_testing_param(data: Series, hypothesized_mean):
    print(f'\n\nH0: Среднее значение генеральной совокупности = {hypothesized_mean}')
    print(f'H1: Среднее значение генеральной совокупности != {hypothesized_mean}')

    # Вычисление коэффициента асимметрии
    skewness = skew(data)

    print('Коэффициент асимметрии:', skewness)

    # Интерпретация результата
    if abs(skewness) < 0.5:
        print("Распределение данных близко к симметричному.")
    elif abs(skewness) < 1:
        print("Распределение данных умеренно асимметрично.")
    else:
        print("Распределение данных сильно асимметрично.")

    print("Используем критерий Вилкоксона:")


    # Вычисление разностей между данными и предполагаемым средним значением
    differences = data - hypothesized_mean

    # Применение критерия Вилкоксона для одной выборки
    statistic, p_value = stats.wilcoxon(differences)

    print('Статистика критерия Вилкоксона:', statistic)
    print('p-значение:', p_value)

    alpha = 0.05

    if p_value < alpha:
        print(f"Так как p value < {alpha} - отклоняем нулевую гипотезу")
    else:
        print(
            f"Так как p value > {alpha} - не отклоняем нулевую гипотезу")

def hypothesis_testing_distr(data: Series):
    print('\n\nH0: Генеральная совокупность распределена нормально')
    print('H1: Генеральная совокупность НЕ распределена нормально')

    alpha = 0.05

    # Проведение теста Шапиро-Уилка
    shapiro_result = shapiro(data   )

    # Извлечение p-value
    p_value = shapiro_result.pvalue

    print(f'Результат теста Шапиро-Уилка: {shapiro_result}')

    if p_value < 0.05:
        print(f"Так как p value < {alpha} - отвергаем нулевую гипотезу")
    else:
        print(f"Так как p value > {alpha} - принимаем нулевую гипотезу")

