import numpy as np
from handlers.DisplacedDispersion import get_displaced_dispersion
from handlers.Mean import get_mean
from handlers.Mode import get_mode
from handlers.NoDisplacedDispersion import get_no_displaced_dispersion
from handlers.Quantiles import get_first_quantile, get_third_quantile
from handlers.SampleSize import get_sample_size
from handlers.StandardDeviation import get_standard_deviation
from models.DataInfo import DataInfo
from models.Quartiles import Quartiles

def handle_data(data):
    info: DataInfo = DataInfo()

    # Объем выборки
    n = get_sample_size(data)
    info.sample_size = n

    # Вариационный ряд
    data = np.sort(data)
    info.variation_series = data

    # Среднее значение
    mean = get_mean(data)
    info.mean = mean

    # Медиана
    median = data[n // 2] if n % 2 != 0 else (data[(n - 1) // 2] + data[(n + 1) // 2]) / 2
    info.median = median

    # Мода
    mode: np.ndarray[float] = get_mode(data)
    info.mode = mode

    # Среднее абсолютное отклонение
    avg_absolute_deviation: float = sum(abs(data_item - mean) for data_item in data) / n
    info.avg_absolute_deviation = avg_absolute_deviation

    # Дисперсия(с отклонением)
    displaced_dispersion = get_displaced_dispersion(data)
    info.displaced_dispersion = displaced_dispersion

    # Дисперсия(без отклонения)
    no_displaced_dispersion = get_no_displaced_dispersion(data)
    info.no_displaced_dispersion = no_displaced_dispersion

    # Минимальное значение
    min_value = min(data)
    info.min_value = min_value

    # Максимальное значение
    max_value = max(data)
    info.max_value = max_value

    # Размах
    spread = max_value - min_value
    info.spread = spread

    # Стандартное отклонение
    standard_deviation = get_standard_deviation(data)
    info.standard_deviation = standard_deviation

    # Квантили(25%, 50%, 75%)
    quartiles: Quartiles = Quartiles()

    # 25%
    quartiles.first_quantile = get_first_quantile(data)

    # Медиана/50%
    quartiles.second_quantile = median

    # 75%
    quartiles.third_quantile = get_third_quantile(data)

    info.quartiles = quartiles

    # Межквартильная широта
    interquartile_range = quartiles.third_quantile - quartiles.first_quantile
    info.interquartile_range = interquartile_range

    return info

