from handlers.Mean import get_mean
from handlers.SampleSize import get_sample_size
from handlers.StandardDeviation import get_standard_deviation


def get_correlation(data1, data2):
    n = get_sample_size(data1)
    if n != get_sample_size(data2):
        return "Ошибка: разные объемы выборок, неверные данные"

    xy_average = sum((data1[i] * data2[i]) for i in range(n)) / n

    return (xy_average - get_mean(data1) * get_mean(data2)) / (get_standard_deviation(data1) * get_standard_deviation(data2))