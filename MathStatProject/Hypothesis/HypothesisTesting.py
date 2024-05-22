from pandas import Series
from constants import round_digits_count
from handlers.Mean import get_mean
from handlers.NoDisplacedDispersion import get_no_displaced_dispersion
from handlers.SampleSize import get_sample_size
import scipy.stats as stats

def hypothesis_testing_param(data: Series, a):
    print(f'\n\nH0: Среднее значение генеральной совокупности = {a}')
    print(f'H1: Среднее значение генеральной совокупности != {a}')
    x_average = get_mean(data)
    n = get_sample_size(data)
    dispersion = get_no_displaced_dispersion(data)
    std = dispersion ** 0.5
    alpha = 0.05
    df = n - 1
    T_nab = (x_average - a) / (std / n**0.5)
    T_crit = stats.t.ppf(1 - alpha / 2, df)
    print(f'Т наблюдаемое =  {round(T_nab, round_digits_count)}')
    print(f'Т критическое =  {round(T_crit, round_digits_count)}')

    if(abs(T_nab) < T_crit):
        print("Так как |Т наблюдаемое| < Т критического, то мы принимаем нулевую гипотезу")
    else:
        print("Так как |Т наблюдаемое| > Т критического, то мы отклоняем нулевую гипотезу")
