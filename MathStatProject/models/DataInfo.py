from numpy import ndarray
from models.Quartiles import Quartiles
from constants import round_digits_count


class DataInfo:
    def __init__(self):
        self.variation_series: ndarray[float]
        self.sample_size: int
        self.mean: float
        self.median: float
        self.displaced_dispersion: float
        self.no_displaced_dispersion: float
        self.quartiles: Quartiles
        self.min_value: float
        self.max_value: float
        self.spread: float
        self.standard_deviation: float
        self.interquartile_range: float
        self.mode: float


    def __str__(self) -> str:
        return (f'Информация о выборке\n'
                f'Объём выборки: {self.sample_size}\n\n'
                f'Среднее по выборке: {self.mean.__round__(round_digits_count)}\n'
                f'Медиана: {self.median.__round__(round_digits_count)}\n'
                f'Мода: {self.mode}\n\n'
                f'Дисперсия(с отклонением): {self.displaced_dispersion.__round__(round_digits_count)}\n'
                f'Дисперсия(без отклонения): {self.no_displaced_dispersion.__round__(round_digits_count)}\n'
                f'Стандартное отклонение: {self.standard_deviation.__round__(round_digits_count)}\n'
                f'{self.quartiles}\n'
                f'Межквартильная широта: {self.interquartile_range.__round__(round_digits_count)}\n\n'
                f'Минимальное значение: {self.min_value.__round__(round_digits_count)}\t'
                f'Максимальное значение: {self.max_value.__round__(round_digits_count)}\n'
                f'Размах: {self.spread.__round__(round_digits_count)}\n\n')
